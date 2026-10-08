# 01 — Foundations: getting text into `Document`s

Nothing downstream works if the loader drops the source. Every chunk you retrieve later should still know which file and page it came from.

## Concepts in this folder

- **Loader.** Turns a file, URL, or table into LangChain `Document`s.
- **`page_content`.** The text that will be chunked and embedded.
- **`metadata`.** `source`, page number, row id. This is the hook for filters and citations.
- **Parsing is not chunking.** A PDF loader gives pages. Chunking happens in module 02.

## Files

| File | What it covers |
| --- | --- |
| `data-ingestion.ipynb` | Text and directory loaders. **Important:** a `Document` is text plus metadata, not a raw string. |
| `parse-pdf.ipynb` | PDF pages via a PDF loader. **Important:** page number belongs in metadata or citations break. |
| `parse-docx.ipynb` | Word documents. **Important:** headings are useful split points later. |
| `parse-csv-excel.ipynb` | Rows as documents. **Important:** one row is often already a chunk; do not re-split a SKU table blindly. |
| `parse-json.ipynb` | JSON and JSONL. **Important:** pick the field that is the body, and keep ids in metadata. |
| `parse-database.ipynb` | SQLite rows. **Important:** SQL is a filter; RAG is for the unstructured column. |
| `sample-data/` | Tiny files the loaders point at. Not a knowledge base. |

The Attention-is-all-you-need PDF that used to sit in `data/pdf/` was a 2 MB paper used only as a loader demo. Use any local PDF, or the arXiv copy, instead of committing it twice.
