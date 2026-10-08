# End-to-end RAG app

Linear LangGraph RAG: load, split, embed, retrieve, answer. The UI is `streamlit_app.py`. The script entry is `main.py`.

Module notes and the loader bug are in [../README.md](../README.md).

```bash
uv sync   # or pip install -r requirements.txt
# put OPENAI_API_KEY in .env
uv run streamlit run streamlit_app.py
```

Graph is `retriever -> responder -> END`. It does not grade or rewrite. That pattern is in `06-rag-patterns/corrective-rag.ipynb`.
