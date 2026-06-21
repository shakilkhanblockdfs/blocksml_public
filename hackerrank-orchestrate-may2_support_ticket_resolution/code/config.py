"""Configuration constants for the support triage agent."""

import os
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
TICKETS_DIR = REPO_ROOT / "support_tickets"
INPUT_CSV = TICKETS_DIR / "support_tickets.csv"
SAMPLE_CSV = TICKETS_DIR / "sample_support_tickets.csv"
OUTPUT_CSV = TICKETS_DIR / "output.csv"

# Domain mappings
COMPANY_TO_DOMAIN = {
    "HackerRank": "hackerrank",
    "hackerrank": "hackerrank",
    "Claude": "claude",
    "claude": "claude",
    "Visa": "visa",
    "visa": "visa",
}

# Allowed output values
ALLOWED_STATUS = {"replied", "escalated"}
ALLOWED_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}

# TF-IDF settings
TFIDF_NGRAM_RANGE = (1, 2)
TFIDF_MAX_DF = 0.85
TFIDF_MIN_DF = 2
TFIDF_SUBLINEAR_TF = True

# Retrieval settings
TOP_K_DOCS = 5
MIN_SIMILARITY_THRESHOLD = 0.02

# LLM settings
ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
LLM_MAX_TOKENS = 1500
LLM_TEMPERATURE = 0
DOC_EXCERPT_MAX_CHARS = 1500
