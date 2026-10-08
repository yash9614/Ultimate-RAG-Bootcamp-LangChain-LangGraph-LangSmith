# 10 — Projects

Two capstones. Read modules 01–04 before the end-to-end app, and module 09 before you change the graph.

## End-to-end app

`end-to-end/` is a small RAG service: load documents, split, embed, retrieve, answer. `streamlit_app.py` is the UI. `main.py` is the script entry.

| Piece | Concept |
| --- | --- |
| `src/document_ingestion/document_processor.py` | Loaders plus `RecursiveCharacterTextSplitter` (500 / 50). **Bug to know:** `load_documents` checks the URL, then ignores `src` and always reads the `data/` folder. `load_from_pdf` also ignores its path. Fix that before you trust it on a new corpus. |
| `src/vectorstore/vectorstore.py` | Build the index and the retriever. |
| `src/state/rag_state.py` | Graph state: question in, answer out. |
| `src/node/nodes.py` | Retrieve and generate. |
| `src/node/reactnode.py` | Same flow with a ReAct-style node. |
| `src/graph_builder/graph_builder.py` | `retriever -> responder -> END`. This is linear RAG, not corrective RAG. |
| `data/url.txt` | Sample URL list. The Attention PDF was removed; it is a public paper, not project data. |

## Graph DB

`graph-db/` is the graph-retrieval lab (Neo4j-style experiments and saved Cypher). Use it when the question is about relationships across entities, not about a single policy paragraph. Vector RAG still wins for "what does section 4 say".
