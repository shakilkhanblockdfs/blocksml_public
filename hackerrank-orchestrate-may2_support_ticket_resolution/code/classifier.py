"""LLM-based ticket classification and response generation."""

import json
import os
import re
import time

import anthropic

from config import ALLOWED_REQUEST_TYPES, ALLOWED_STATUS, ANTHROPIC_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE
from models import CorpusDoc, Ticket, TriageResult
from prompts import SYSTEM_PROMPT, build_user_prompt


def _parse_json_response(text: str) -> dict:
    """Extract JSON from LLM response, handling markdown fences."""
    # Try direct parse
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting from markdown code block
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # Try finding any JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    return {}


def _validate_result(data: dict) -> TriageResult:
    """Validate and normalize the parsed LLM output."""
    status = str(data.get("status", "escalated")).lower().strip()
    if status not in ALLOWED_STATUS:
        status = "escalated"

    request_type = str(data.get("request_type", "product_issue")).lower().strip()
    if request_type not in ALLOWED_REQUEST_TYPES:
        request_type = "product_issue"

    product_area = str(data.get("product_area", "general")).lower().strip()
    response = str(data.get("response", "This issue has been escalated to a human agent."))
    justification = str(data.get("justification", "Unable to parse LLM response; escalating as safe default."))

    return TriageResult(
        status=status,
        product_area=product_area,
        response=response,
        justification=justification,
        request_type=request_type,
    )


def classify_ticket(
    ticket: Ticket,
    docs_with_scores: list[tuple[CorpusDoc, float]],
    client: anthropic.Anthropic,
) -> TriageResult:
    """Classify a ticket and generate a response using the LLM."""
    user_prompt = build_user_prompt(ticket, docs_with_scores)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=LLM_MAX_TOKENS,
                temperature=LLM_TEMPERATURE,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
            )
            response_text = response.content[0].text
            parsed = _parse_json_response(response_text)

            if parsed:
                return _validate_result(parsed)

            # If parsing failed, escalate as safe default
            return TriageResult(
                status="escalated",
                product_area="general",
                response="This issue has been escalated to a human agent for further assistance.",
                justification="Unable to parse automated response; escalating for safety.",
                request_type="product_issue",
            )

        except anthropic.RateLimitError:
            if attempt < max_retries - 1:
                wait_time = 2 ** (attempt + 1)
                print(f"  Rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
            raise

        except anthropic.APIError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** (attempt + 1)
                print(f"  API error: {e}, retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue

            return TriageResult(
                status="escalated",
                product_area="general",
                response="This issue has been escalated to a human agent for further assistance.",
                justification=f"API error during processing; escalating for safety.",
                request_type="product_issue",
            )
