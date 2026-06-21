"""Multi-Domain Support Triage Agent — Main Entry Point.

Processes support tickets from CSV using RAG over a support corpus
and outputs classified, grounded responses.

Usage:
    python code/main.py                          # Process support_tickets.csv
    python code/main.py --sample                 # Process sample_support_tickets.csv (for validation)
    python code/main.py --input path/to/file.csv # Process a custom CSV
"""

import argparse
import csv
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load .env from repo root
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

import anthropic

from config import DATA_DIR, INPUT_CSV, OUTPUT_CSV, SAMPLE_CSV
from indexer import build_index
from models import Ticket, TriageResult
from retriever import retrieve_docs
from classifier import classify_ticket


def read_tickets(csv_path: Path) -> list[Ticket]:
    """Read tickets from a CSV file."""
    tickets = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            ticket = Ticket(
                issue=row.get("Issue", "").strip(),
                subject=row.get("Subject", "").strip(),
                company=row.get("Company", "").strip(),
                row_index=i,
            )
            tickets.append(ticket)
    return tickets


def write_output(tickets: list[Ticket], results: list[TriageResult], output_path: Path):
    """Write triage results to CSV."""
    fieldnames = [
        "issue", "subject", "company",
        "status", "product_area", "response", "justification", "request_type",
    ]

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for ticket, result in zip(tickets, results):
            writer.writerow({
                "issue": ticket.issue,
                "subject": ticket.subject,
                "company": ticket.company,
                "status": result.status.capitalize(),
                "product_area": result.product_area,
                "response": result.response,
                "justification": result.justification,
                "request_type": result.request_type,
            })


def main():
    parser = argparse.ArgumentParser(description="Multi-Domain Support Triage Agent")
    parser.add_argument("--sample", action="store_true", help="Run against sample tickets for validation")
    parser.add_argument("--input", type=str, help="Path to input CSV file")
    parser.add_argument("--output", type=str, help="Path to output CSV file")
    args = parser.parse_args()

    # Determine input/output paths
    if args.input:
        input_path = Path(args.input)
    elif args.sample:
        input_path = SAMPLE_CSV
    else:
        input_path = INPUT_CSV

    output_path = Path(args.output) if args.output else OUTPUT_CSV

    # Validate API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set. Set it in .env or as an environment variable.")
        sys.exit(1)

    print("=" * 60)
    print("Multi-Domain Support Triage Agent")
    print("=" * 60)

    # Step 1: Build corpus index
    index = build_index(DATA_DIR)
    print()

    # Step 2: Read tickets
    print(f"Reading tickets from {input_path}...")
    tickets = read_tickets(input_path)
    print(f"Loaded {len(tickets)} tickets")
    print()

    # Step 3: Initialize Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # Step 4: Process each ticket
    results = []
    print("Processing tickets...")
    print("-" * 60)

    for i, ticket in enumerate(tickets):
        company_display = ticket.company if ticket.company and ticket.company.strip().lower() != "none" else "?"
        print(f"[{i+1}/{len(tickets)}] {company_display} | {ticket.subject[:50] if ticket.subject else '(no subject)'}...")

        # Retrieve relevant docs
        docs_with_scores = retrieve_docs(ticket, index)
        top_score = docs_with_scores[0][1] if docs_with_scores else 0.0

        # Classify and generate response
        result = classify_ticket(ticket, docs_with_scores, client)
        results.append(result)

        print(f"        → {result.status} | {result.request_type} | {result.product_area} (top_score={top_score:.3f})")

    print("-" * 60)

    # Step 5: Write output
    print(f"\nWriting results to {output_path}...")
    write_output(tickets, results, output_path)

    # Summary
    replied_count = sum(1 for r in results if r.status == "replied")
    escalated_count = sum(1 for r in results if r.status == "escalated")
    print(f"\nDone! {len(results)} tickets processed:")
    print(f"  Replied:   {replied_count}")
    print(f"  Escalated: {escalated_count}")
    print(f"  Request types: {dict((rt, sum(1 for r in results if r.request_type == rt)) for rt in set(r.request_type for r in results))}")


if __name__ == "__main__":
    main()
