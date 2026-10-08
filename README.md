# Ultimate RAG Bootcamp — LangChain, LangGraph, LangSmith

Reorganized study repo for retrieval-augmented generation. The old dump
(`Ultimate-gar-Bootcamp-Using-angchain-angGraph-Lngsmith`) mixed notebooks,
duplicate `(1)` copies, and multi-megabyte slide PDFs in one folder. This
repo keeps one copy of each notebook, groups them by concept, and documents
what each file is teaching.

Slide decks were not copied. They stay in the old repo. The concept each
deck covered is listed in [reference/slides.md](reference/slides.md).

## How to use this

Work the folders in order. Each folder README names the RAG idea, the file
that demonstrates it, and what to look for in that file.

```bash
# install uv if you do not have it: https://docs.astral.sh/uv/
uv sync
cp .env.example .env
# fill OPENAI_API_KEY and TAVILY_API_KEY in .env
uv run jupyter lab
```

This repo is a uv project (`pyproject.toml`). `uv sync` creates `.venv` here and installs dependencies. Run notebooks and scripts with `uv run` so an already-activated venv from another folder is ignored.

Windows PowerShell:

```powershell
uv sync
copy .env.example .env
uv run jupyter lab
```

If another project's venv is active, uv warns that `VIRTUAL_ENV` does not match `.venv` and ignores it. That is what you want. Do not pass `--active` unless you mean to use the other environment.

Keys stay in `.env` only. Notebooks must read them with `load_dotenv()` and `os.getenv`. A few notebooks also use Groq, Hugging Face, Pinecone, or Astra.

## Map

| Order | Folder | Concepts |
| --- | --- | --- |
| 01 | [foundations](01-foundations/README.md) | loaders, `Document`, metadata |
| 02 | [chunking](02-chunking/README.md) | fixed, recursive, semantic chunking |
| 03 | [embeddings and stores](03-embeddings-and-vector-stores/README.md) | embeddings, Chroma, FAISS, Pinecone |
| 04 | [retrieval](04-retrieval/README.md) | dense, sparse, hybrid, RRF, MMR, rerank |
| 05 | [query transforms](05-query-transforms/README.md) | expansion, decomposition, HyDE |
| 06 | [RAG patterns](06-rag-patterns/README.md) | corrective, adaptive, iterative, CAG |
| 07 | [agentic RAG](07-agentic-rag/README.md) | grade, rewrite, retrieve loop |
| 08 | [evaluation and memory](08-evaluation-and-memory/README.md) | faithfulness, relevance, chat memory |
| 09 | [LangGraph and agents](09-langgraph-and-agents/README.md) | state, ReAct, multi-agent |
| 10 | [projects](10-projects/README.md) | end-to-end app, graph RAG |

Concept glossary: [reference/concepts.md](reference/concepts.md).

## What changed from the old repo

- Duplicate `(1)` notebooks and PDFs removed.
- `EnsembleRetriever` still lives in `04-retrieval/hybrid-dense-sparse.ipynb`. The explicit RRF formula, which that notebook never prints, is in `04-retrieval/hybrid_rrf.py`.
- The end-to-end loader used to ignore the path you passed and always read `data/`. That is noted in the project README.
