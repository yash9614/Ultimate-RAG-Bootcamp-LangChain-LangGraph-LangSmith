# RAG concept glossary

Short definitions used across the module READMEs.

- **Document.** LangChain unit of text plus metadata (`source`, `page`, `team`). Metadata is what later filters use.
- **Chunk.** A slice of a document small enough to embed and retrieve. Too large and the vector is muddy. Too small and the fact is cut in half.
- **Chunk overlap.** Characters shared by neighboring chunks so a sentence on the boundary is not lost.
- **Embedding.** A vector for a chunk. Similar meaning should land nearby. Exact IDs often do not.
- **Dense retrieval.** Nearest neighbors in embedding space. Good for paraphrases.
- **Sparse retrieval / BM25.** Term frequency ranking. Good for error codes, SKUs, names.
- **Hybrid retrieval.** Run dense and sparse, then fuse. They fail in different ways.
- **RRF.** Reciprocal rank fusion. Score is `sum 1/(k + rank)` with `k` usually 60. Ignores raw scores, which is the point: cosine and BM25 are not comparable.
- **MMR.** Maximal marginal relevance. Penalizes chunks that are near the query but also near each other, so the context is not five copies of the same paragraph.
- **Reranking.** A cross-encoder scores the query and a candidate together. Slow, so it runs only on the top 20–50 after retrieval.
- **Metadata filter.** Restrict search to `team=hr` or `source=leave_policy.md` before or during retrieval.
- **Query expansion.** Generate extra phrasings, retrieve for each, then fuse.
- **Query decomposition.** Split a multi-hop question into sub-questions.
- **HyDE.** Embed a hypothetical answer, then search with that vector instead of the raw question.
- **Corrective RAG.** Grade retrieved docs. If they are irrelevant, rewrite the query or fall back to web search.
- **Adaptive RAG.** Route the question: no retrieval, vector retrieval, or web, depending on the question.
- **Iterative retrieval.** Retrieve, look at the gap, retrieve again.
- **Self-reflection.** The model critiques its own answer against the context.
- **CAG.** Cache-augmented generation. Put a stable knowledge cache in the prompt instead of retrieving every time.
- **Vectorless / PageIndex.** Retrieve by document structure (sections, pages) instead of embeddings.
- **Agentic RAG.** A graph decides when to retrieve, grade, and rewrite. Retrieval is a tool, not a fixed first step.
- **Faithfulness.** The answer is supported by the retrieved context.
- **Answer relevance.** The answer addresses the question.
- **Context precision / recall.** The retrieved set contains the right chunks and not too much junk.
