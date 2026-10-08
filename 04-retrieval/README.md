# 04 — Retrieval

This is the module that decides which chunks the model is allowed to see.

## Concepts

- **Top-k.** How many chunks you return. Bigger k helps recall and hurts the prompt.
- **Dense only.** Paraphrases work. Exact codes often fail.
- **BM25 only.** Exact tokens work. Paraphrases fail.
- **Hybrid.** Both lists.
- **RRF.** Fuse by rank, not by score. Formula and a worked example are in `hybrid_rrf.py`. LangChain's `EnsembleRetriever` is weighted RRF with constant `c=60`. The notebook calls it without saying so.
- **MMR.** Diversity. Use it when the top hits are near-duplicates.
- **Rerank.** Second stage. Retrieve 30, rerank, keep 4.

## Files

| File | What it covers |
| --- | --- |
| `hybrid-dense-sparse.ipynb` | FAISS + BM25 + `EnsembleRetriever`. **Important:** the constructor argument is `weights`, not `weight`. The saved run shows `weights=[0.5, 0.5]`, so the 0.7/0.3 line did not apply. |
| `hybrid_rrf.py` | Explicit `1/(k+rank)` and weighted RRF. Run with `python hybrid_rrf.py`. Rank 1 in both lists scores about `0.0328` when `k=60`. |
| `mmr.ipynb` | `search_type="mmr"`. **Important:** lambda trades relevance against novelty. |
| `reranking.ipynb` | Cross-encoder over retrieved candidates. **Important:** rerank does not search the corpus. It only reorders what retrieval already returned. |

A zero BM25 score can still occupy rank 1 if every document scored zero. RRF will treat that rank as real. Drop zero-score hits before fusion if the token is missing.
