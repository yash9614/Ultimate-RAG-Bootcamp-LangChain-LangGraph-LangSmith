# End-to-end RAG app

Linear LangGraph RAG: load, split, embed, retrieve, answer. The UI is `streamlit_app.py`. The script entry is `main.py`.

Module notes and the loader bug are in [../README.md](../README.md).

From the repo root, `uv sync` once. This app has its own `pyproject.toml`, so run it from this folder:

```bash
uv sync
# OPENAI_API_KEY in this folder's .env, or the repo-root .env
uv run streamlit run streamlit_app.py
```

Graph is `retriever -> responder -> END`. It does not grade or rewrite. That pattern is in `06-rag-patterns/corrective-rag.ipynb`.
