# 06 — RAG patterns

Same index, different control flow around it.

## Concepts

- **Stuff.** Put the retrieved chunks in one prompt. Default, and what the hybrid notebook does.
- **Corrective (CRAG).** A grader rejects bad chunks, then the graph rewrites or searches the web.
- **Self-RAG.** Model decides whether retrieval is needed and critiques both passages and its own answer.
- **Adaptive.** A router skips retrieval for chit-chat and uses it for policy questions.
- **Chain-of-thought RAG.** Reason over the chunks before the final sentence.
- **Iterative / Agentic RAG.** Agent controls retrieval — can retrieve multiple times, decompose, stop when sufficient.
- **Self-reflection.** Check the draft against the context.
- **CAG.** Skip retrieval when the knowledge already fits in a cache.
- **Vectorless.** Walk a page or section index instead of an embedding index.
- **Multimodal.** Retrieve images or pages, not only text.
- **GraphRAG.** Knowledge graph + community summaries for relational / multi-hop questions.

## Files

| File | What it covers |
| --- | --- |
| `answer-synthesis.ipynb` | How retrieved docs become the `{context}` block. **Important:** the prompt must say to abstain when the context is empty. |
| `corrective-rag.ipynb` | Grade documents, rewrite, optional web fallback. **Important:** the grader is a retrieval fix, not a generation fix. |
| `adaptive-rag.ipynb` | Route by question type. **Important:** a router mistake skips the index entirely. |
| `chain-of-thought-rag.ipynb` | Stepwise answer grounded in chunks. |
| `iterative-retrieval.ipynb` | Retrieve, assess, retrieve again. **Important:** cap the loop. |
| `self-reflection.ipynb` | Critique node after generation. |
| `cache-augmented-generation.ipynb` | CAG. **Important:** the cache goes stale. It is not a substitute for an index that changes daily. |
| `vectorless-pageindex.ipynb` | PageIndex-style retrieval without vectors. **Important:** this wins on long structured docs, not on a pile of chats. |
| `multimodal-rag.ipynb` | OpenAI multimodal inputs. **Important:** an image still needs a citation back to the source file. |

## Deeper Notes

Full comparison of Naive / Hybrid / Self-RAG / CRAG / Agentic RAG / GraphRAG:

**[makan_m/learning-concepts/17-advanced-rag-patterns.md](https://github.com/yash9614/makan_m/blob/main/learning-concepts/17-advanced-rag-patterns.md)**
