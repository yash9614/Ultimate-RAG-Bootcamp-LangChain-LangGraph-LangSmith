# 07 — Agentic RAG

Agentic RAG is a graph with a retrieve tool, a relevance grade, and a rewrite edge. It is not a different embedding.

## Concepts

- **Retrieve node.** Same retriever as module 04.
- **Grade node.** Binary or scored relevance. Irrelevant docs should not reach the prompt.
- **Rewrite node.** New query from the question plus the failure.
- **Generate node.** Only after the grade passes.
- **Stop condition.** Max rewrites, otherwise the loop burns tokens.

## Files

| File | What it covers |
| --- | --- |
| `agentic-rag.ipynb` | Smaller agentic loop. **Important:** retrieval is a step the graph can repeat. |
| `agentic-rag-langgraph.ipynb` | Longer LangGraph version of the same idea. **Important:** state must carry the question, the docs, and the retry count. Read this after module 09 if the graph API is unfamiliar. |

These two notebooks overlapped in the old repo (`1-agenticrag.ipynb` and `1-AgenticRAG (1).ipynb`). Both are kept because they are not the same file.
