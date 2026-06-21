"""Data models for the support triage agent."""

from dataclasses import dataclass, field


@dataclass
class CorpusDoc:
    """A single document from the support corpus."""
    path: str
    domain: str  # "claude" | "hackerrank" | "visa"
    title: str
    source_url: str
    breadcrumbs: list[str] = field(default_factory=list)
    content: str = ""

    @property
    def product_area(self) -> str:
        """Derive product area from breadcrumbs or path."""
        if self.breadcrumbs:
            return self.breadcrumbs[0]
        # Fallback: use directory name
        parts = self.path.split("/")
        for i, part in enumerate(parts):
            if part in ("claude", "hackerrank", "visa") and i + 1 < len(parts):
                return parts[i + 1]
        return "general"


@dataclass
class Ticket:
    """A support ticket input."""
    issue: str
    subject: str
    company: str  # "HackerRank", "Claude", "Visa", "None", or ""
    row_index: int = 0


@dataclass
class TriageResult:
    """The triage output for a single ticket."""
    status: str  # "replied" | "escalated"
    product_area: str
    response: str
    justification: str
    request_type: str  # "product_issue" | "feature_request" | "bug" | "invalid"
