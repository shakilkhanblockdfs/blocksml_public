"""Corpus loading and TF-IDF index construction."""

import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer

from config import (
    DATA_DIR,
    TFIDF_MAX_DF,
    TFIDF_MIN_DF,
    TFIDF_NGRAM_RANGE,
    TFIDF_SUBLINEAR_TF,
)
from models import CorpusDoc


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown text.

    Returns (metadata_dict, body_text).
    Uses simple parsing to avoid pyyaml dependency.
    """
    if not text.startswith("---"):
        return {}, text

    end_idx = text.find("---", 3)
    if end_idx == -1:
        return {}, text

    frontmatter_str = text[3:end_idx].strip()
    body = text[end_idx + 3:].strip()

    metadata = {}
    current_key = None
    current_value_lines = []
    in_list = False

    for line in frontmatter_str.split("\n"):
        stripped = line.strip()

        # List item
        if stripped.startswith("- ") and current_key:
            if current_key not in metadata:
                metadata[current_key] = []
            val = stripped[2:].strip().strip('"').strip("'")
            if isinstance(metadata[current_key], list):
                metadata[current_key].append(val)
            continue

        # Key-value pair
        if ":" in stripped and not stripped.startswith("-"):
            # Save previous key
            if current_key and current_key not in metadata:
                metadata[current_key] = " ".join(current_value_lines).strip().strip('"').strip("'")

            colon_idx = stripped.index(":")
            current_key = stripped[:colon_idx].strip()
            val = stripped[colon_idx + 1:].strip().strip('"').strip("'")
            current_value_lines = [val] if val else []
            in_list = False
        elif current_key and current_key not in metadata:
            current_value_lines.append(stripped)

    # Save last key
    if current_key and current_key not in metadata:
        metadata[current_key] = " ".join(current_value_lines).strip().strip('"').strip("'")

    return metadata, body


def strip_markdown(text: str) -> str:
    """Remove markdown formatting, keep plain text."""
    # Remove images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Remove links but keep text
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)
    # Remove headers markers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,3}([^_]+)_{1,3}", r"\1", text)
    # Remove horizontal rules
    text = re.sub(r"^-{3,}$", "", text, flags=re.MULTILINE)
    # Remove blockquotes
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    # Remove table separators
    text = re.sub(r"\|", " ", text)
    # Collapse whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def detect_domain(filepath: Path) -> str:
    """Detect domain from file path."""
    parts = filepath.parts
    for part in parts:
        if part in ("claude", "hackerrank", "visa"):
            return part
    return "unknown"


def load_corpus(data_dir: Path = DATA_DIR) -> list[CorpusDoc]:
    """Load all markdown files from the data directory."""
    docs = []
    md_files = sorted(data_dir.rglob("*.md"))

    for filepath in md_files:
        try:
            text = filepath.read_text(encoding="utf-8")
        except Exception:
            continue

        metadata, body = parse_frontmatter(text)
        domain = detect_domain(filepath)

        title = metadata.get("title", filepath.stem.replace("-", " ").title())
        source_url = metadata.get("source_url", "")

        breadcrumbs_raw = metadata.get("breadcrumbs", [])
        if isinstance(breadcrumbs_raw, str):
            breadcrumbs = [breadcrumbs_raw] if breadcrumbs_raw else []
        else:
            breadcrumbs = breadcrumbs_raw

        plain_text = strip_markdown(body)
        if not plain_text.strip():
            continue

        doc = CorpusDoc(
            path=str(filepath),
            domain=domain,
            title=title,
            source_url=source_url,
            breadcrumbs=breadcrumbs,
            content=plain_text,
        )
        docs.append(doc)

    return docs


class CorpusIndex:
    """TF-IDF index over the support corpus."""

    def __init__(self, docs: list[CorpusDoc]):
        self.docs = docs
        self.vectorizer = TfidfVectorizer(
            ngram_range=TFIDF_NGRAM_RANGE,
            max_df=TFIDF_MAX_DF,
            min_df=TFIDF_MIN_DF,
            sublinear_tf=TFIDF_SUBLINEAR_TF,
            stop_words="english",
        )
        # Build index: combine title + content for richer matching
        corpus_texts = [f"{doc.title} {doc.content}" for doc in docs]
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus_texts)

        # Pre-compute domain indices for fast filtering
        self.domain_indices: dict[str, list[int]] = {}
        for i, doc in enumerate(docs):
            self.domain_indices.setdefault(doc.domain, []).append(i)

    def get_domain_docs(self, domain: str | None) -> tuple[list[int], list[CorpusDoc]]:
        """Get document indices and docs for a domain. None = all domains."""
        if domain and domain in self.domain_indices:
            indices = self.domain_indices[domain]
            return indices, [self.docs[i] for i in indices]
        # Return all
        return list(range(len(self.docs))), self.docs


def build_index(data_dir: Path = DATA_DIR) -> CorpusIndex:
    """Load corpus and build TF-IDF index."""
    print(f"Loading corpus from {data_dir}...")
    docs = load_corpus(data_dir)
    print(f"Loaded {len(docs)} documents")
    print(f"  - claude: {sum(1 for d in docs if d.domain == 'claude')}")
    print(f"  - hackerrank: {sum(1 for d in docs if d.domain == 'hackerrank')}")
    print(f"  - visa: {sum(1 for d in docs if d.domain == 'visa')}")

    print("Building TF-IDF index...")
    index = CorpusIndex(docs)
    print(f"Index built: {index.tfidf_matrix.shape[0]} docs, {index.tfidf_matrix.shape[1]} features")
    return index
