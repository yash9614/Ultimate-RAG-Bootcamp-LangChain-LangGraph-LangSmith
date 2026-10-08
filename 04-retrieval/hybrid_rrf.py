"""Hybrid retrieval with explicit Reciprocal Rank Fusion.

Dense scores (cosine) and BM25 scores are not on the same scale, so this
module never adds them. It fuses ranked lists by position:

    RRF(d) = sum over lists of 1 / (k + rank(d))

k is a smoothing constant, conventionally 60. It is not a top-k.
"""

from __future__ import annotations

from collections import defaultdict


def reciprocal_rank_fusion(ranked_lists: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    """Fuse lists of document ids. Rank 1 is the best hit in each list."""
    scores: dict[str, float] = defaultdict(float)
    for ranking in ranked_lists:
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)


def weighted_rrf(
    ranked_lists: list[list[str]],
    weights: list[float] | None = None,
    k: int = 60,
) -> list[tuple[str, float]]:
    """Same as RRF, but each list is scaled by a weight. This is what
    LangChain EnsembleRetriever does (parameter name is `weights`, constant `c`).
    """
    if weights is None:
        weights = [1.0] * len(ranked_lists)
    if len(weights) != len(ranked_lists):
        raise ValueError("weights must match the number of ranked lists")
    scores: dict[str, float] = defaultdict(float)
    for ranking, weight in zip(ranked_lists, weights):
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] += weight / (k + rank)
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)


if __name__ == "__main__":
    dense = ["shipping-tracking", "shipping-sla", "warranty"]
    sparse = ["shipping-tracking", "error-4022", "error-timeout"]
    print("plain RRF")
    for doc_id, score in reciprocal_rank_fusion([dense, sparse]):
        print(f"  {score:.4f}  {doc_id}")
    print("weighted RRF 0.7 dense / 0.3 sparse")
    for doc_id, score in weighted_rrf([dense, sparse], weights=[0.7, 0.3]):
        print(f"  {score:.4f}  {doc_id}")
