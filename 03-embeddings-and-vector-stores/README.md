# 03 — Embeddings and vector stores

An embedding model and a vector store are different choices. You can swap the store and keep the same model. You cannot mix vectors from two models in one index.

## Concepts

- **Bi-encoder.** Query and chunk are embedded separately. Fast enough to scan a corpus. This is dense retrieval.
- **Normalization / cosine vs dot product.** Pick one metric and stick to it. FAISS inner product on normalized vectors is cosine.
- **Local index.** Chroma or FAISS on disk. Fine for a course and a single process.
- **Hosted database.** Pinecone, Astra. Same idea, plus filtering and scale.
- **Persistence.** If you rebuild the index every run, you are not learning retrieval, you are learning load time.

## Files

| File | What it covers |
| --- | --- |
| `embeddings.ipynb` | Hugging Face sentence embeddings. **Important:** the model name is part of the index identity. |
| `openai-embeddings.ipynb` | `text-embedding-3-small` / OpenAI vectors. **Important:** do not compare these distances to MiniLM distances. |
| `chromadb.ipynb` | Chroma collection, add, query. **Important:** metadata filters are a Chroma `where` clause. |
| `faiss.ipynb` | FAISS index and `as_retriever()`. **Important:** FAISS here is an index, not a database. |
| `other-vector-stores.ipynb` | Same retriever API, different backend. |
| `pinecone.ipynb` | Hosted index. **Important:** namespace and metadata are how you isolate tenants. |
| `datastax-astradb.ipynb` | Astra as another hosted store. Same lesson as Pinecone. |
