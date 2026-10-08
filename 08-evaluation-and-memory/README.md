# 08 — Evaluation and memory

If you cannot tell a bad retrieval from a bad answer, you will tune the wrong knob.

## Concepts

- **Retrieval metrics.** Hit rate, recall@k, MRR. Needs a labeled question-to-chunk set.
- **Generation metrics.** Faithfulness (supported by context), answer relevance (about the question).
- **RAGAS-style eval.** LLM-as-judge on those axes. Noisy, but better than eyeballing one demo query.
- **Memory.** Chat history is not the knowledge base. Put history in the question rewrite, and keep the index for documents.

## Files

| File | What it covers |
| --- | --- |
| `rag-evaluation.ipynb` | Eval harness for a RAG chain. **Important:** score retrieval and generation separately. |
| `conversation-memory.ipynb` | Memory in front of retrieval. **Important:** do not embed the whole transcript into the same collection as your policies. |
| `sample-rag-dataset.txt` | Tiny labeled-style notes used as demo data, not a benchmark. |
