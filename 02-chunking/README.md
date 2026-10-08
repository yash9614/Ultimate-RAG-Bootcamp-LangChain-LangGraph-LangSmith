# 02 — Chunking

Retrieval quality is mostly a chunking problem. The embedding cannot find a fact that was split across two chunks with no overlap, and it cannot prefer a fact buried in a 2,000-token blob.

## Concepts

- **Fixed-size chunking.** `chunk_size` characters or tokens. Simple, blunt.
- **Recursive character splitting.** Try paragraphs, then lines, then spaces, so you do not cut mid-word if you can avoid it. This is what `RecursiveCharacterTextSplitter` does. The end-to-end project uses size 500 and overlap 50.
- **Overlap.** Typically 10–20% of the chunk. Keeps a sentence that sits on the boundary.
- **Semantic chunking.** Split where the embedding of the next sentence jumps. Better topic boundaries, more compute at index time.
- **Structure-aware chunking.** Split on markdown headings or HTML sections. Best when the source has headings.

## Files

| File | What it covers |
| --- | --- |
| `semantic-chunking.ipynb` | Semantic splits with an embedding model. **Important:** this replaces a fixed window only when neighboring sentences change topic. It does not replace metadata. |

There is no separate notebook for recursive splitting. It shows up as the default splitter in `10-projects/end-to-end/src/document_ingestion/document_processor.py`.

Rule of thumb from the hybrid lab: 150 characters was a teaching size so the terminal could show a chunk. Production chunks are usually a few hundred tokens, not 150 characters.
