# Multi-Domain Support Triage Agent

A terminal-based support triage agent that classifies and responds to support tickets across three ecosystems: HackerRank, Claude (Anthropic), and Visa.

## Architecture

**3-stage RAG pipeline:**

1. **Index** — Loads 774 markdown corpus files, parses YAML frontmatter, builds a TF-IDF index using scikit-learn
2. **Retrieve** — Domain-filtered cosine similarity search returns top-5 relevant docs per ticket
3. **Classify + Respond** — Single Claude API call per ticket with retrieved context produces structured JSON output (status, product_area, response, justification, request_type)

### Design Decisions

- **TF-IDF over embeddings**: Free, fast, fully deterministic, and effective for keyword-heavy support queries
- **Domain pre-filtering**: Filters corpus by Company column before retrieval to reduce noise
- **Single LLM call**: Joint classification + response generation for coherent output
- **Safe defaults**: Escalates on parsing failures or API errors

## Setup

```bash
# Install dependencies
pip install -r code/requirements.txt

# Set API key (copy .env.example to .env and add your key)
cp .env.example .env
# Edit .env and set ANTHROPIC_API_KEY=sk-ant-...
```

## Usage

```bash
# Process the main support tickets
python code/main.py

# Validate against sample tickets
python code/main.py --sample

# Custom input/output
python code/main.py --input path/to/input.csv --output path/to/output.csv
```

## File Structure

```
code/
  main.py          — Entry point, pipeline orchestration, CSV I/O
  indexer.py        — Corpus loading, YAML frontmatter parsing, TF-IDF index
  retriever.py      — Domain-filtered cosine similarity search
  classifier.py     — LLM API call, JSON parsing, validation
  prompts.py        — System and user prompt templates
  models.py         — Data models (CorpusDoc, Ticket, TriageResult)
  config.py         — Paths, constants, model settings
  requirements.txt  — Python dependencies
```

## Output Format

The agent produces `support_tickets/output.csv` with columns:
- `status`: "Replied" or "Escalated"
- `product_area`: Support category (e.g., "screen", "privacy", "general_support")
- `response`: User-facing answer grounded in corpus documentation
- `justification`: Reasoning for the triage decision
- `request_type`: "product_issue", "feature_request", "bug", or "invalid"
