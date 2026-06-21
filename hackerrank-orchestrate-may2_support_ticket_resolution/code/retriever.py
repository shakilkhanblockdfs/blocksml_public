"""Domain-filtered document retrieval using TF-IDF cosine similarity."""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from config import COMPANY_TO_DOMAIN, MIN_SIMILARITY_THRESHOLD, TOP_K_DOCS
from indexer import CorpusIndex
from models import CorpusDoc, Ticket


def retrieve_docs(
    ticket: Ticket,
    index: CorpusIndex,
    top_k: int = TOP_K_DOCS,
) -> list[tuple[CorpusDoc, float]]:
    """Retrieve the most relevant documents for a ticket.

    Returns list of (doc, similarity_score) tuples, sorted by score descending.
    """
    # Build query from issue + subject
    query_parts = [ticket.issue]
    if ticket.subject and ticket.subject.strip():
        query_parts.append(ticket.subject)
    query = " ".join(query_parts)

    # Determine domain filter
    company = ticket.company.strip() if ticket.company else ""
    domain = COMPANY_TO_DOMAIN.get(company)

    # Get domain-filtered indices
    if domain:
        candidate_indices = index.domain_indices.get(domain, [])
    else:
        candidate_indices = list(range(len(index.docs)))

    if not candidate_indices:
        # Fallback to all docs
        candidate_indices = list(range(len(index.docs)))

    # Vectorize query
    query_vec = index.vectorizer.transform([query])

    # Compute similarity only against candidates
    candidate_matrix = index.tfidf_matrix[candidate_indices]
    similarities = cosine_similarity(query_vec, candidate_matrix).flatten()

    # Sort by similarity
    sorted_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in sorted_indices:
        score = float(similarities[idx])
        if score < MIN_SIMILARITY_THRESHOLD and len(results) > 0:
            break  # Stop if below threshold (but always include at least 1)
        doc = index.docs[candidate_indices[idx]]
        results.append((doc, score))

    return results
