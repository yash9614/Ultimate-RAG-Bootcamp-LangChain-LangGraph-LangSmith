# 05 — Query transforms

Sometimes the question is the weak part, not the index.

## Concepts

- **Expansion / multi-query.** Several phrasings, one fusion step. RRF is the natural merge, same as module 04.
- **Decomposition.** One question that needs two facts becomes two searches.
- **Planning.** An LLM writes the sub-questions instead of a fixed template.
- **HyDE.** Generate a fake answer, embed that, search. Helps when the question is short and the documents are long.

## Files

| File | What it covers |
| --- | --- |
| `query-expansion.ipynb` | Extra queries from an LLM, then retrieve. **Important:** fuse the lists. Do not stuff every list into the prompt. |
| `query-decomposition.ipynb` | Split a compound question. **Important:** answer sub-questions before the final synthesis. |
| `query-planning.ipynb` | Planner that emits a retrieval plan. **Important:** the plan is data, not the answer. |
| `hyde.ipynb` | Hypothetical document embedding. **Important:** the hypothetical text is a query, not a source you cite. |
