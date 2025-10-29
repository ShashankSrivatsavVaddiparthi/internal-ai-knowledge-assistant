---
title: Internal_AI_Knowledge_Assistant
---

# Internal AI Knowledge Assistant

A sophisticated AI-powered knowledge assistant built to help organizations manage and retrieve internal information efficiently.

## Overview

This project implements an intelligent assistant that uses advanced AI techniques to process, understand, and retrieve information from internal knowledge bases.

## Features

- Natural language query processing
- Semantic search capabilities
- Real-time response generation
- Document context understanding
- Custom knowledge base integration

## Setup

### Prerequisites
- Python 3.8+
- uv package manager

### Installation
1. Clone the repository
2. Install dependencies:
    ```bash
    uv pip install .
    ```

## Usage

Run the application using:
```bash
python src/main.py
```

## Project Structure

```
.
├── data/
│   ├── processed/          # Processed text files from PDFs
│   ├── uploads/           # Original PDF documents
│   └── vectors/           # Vector store indexes
│       └── iaka_index/
│           └── index.faiss
├── src/
│   ├── ingestion/        # File upload and processing
│   │   └── upload_router.py
│   ├── parsing/          # Document parsing services
│   │   └── parser_service.py
│   ├── rag/             # Retrieval Augmented Generation
│   │   └── retriever_service.py
│   ├── ui/              # User interface
│   │   └── app.py
│   ├── vectorstore/     # Vector storage management
│   │   └── vector_service.py
│   └── main.py          # Application entry point
├── pyproject.toml       # Project dependencies and configuration
└── README.md
```
## Development Roadmap

The following table outlines the planned development phases and features for the Internal AI Knowledge Assistant. Phase 0 is the current MVP.

| **Phase**   | **Title**                     | **Goal / Objective**                                                            | **Core Tasks**                                                                                                                                                    | **Key Tools / Libraries**                                                                       | **Expected Outcome**                                              |
| ----------- | ----------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Phase 0** | MVP                           | Baseline project (current state): PDF ingestion, FAISS vector store, basic UI.  | - Handle PDF uploads and extraction.<br>- Chunking & embeddings.<br>- FAISS indexing.<br>- Basic query endpoint and Gradio/FastAPI UI.                          | `faiss-cpu`, `langchain`, `sentence-transformers`, `fastapi`, `gradio`, `pymupdf`, `unstructured` | Working MVP: PDF ingestion + semantic search + basic UI        |
| **Phase 1** | Multi-format Document Loading | Expand ingestion pipeline to handle multiple file types beyond PDFs.            | - Integrate loaders for DOCX, TXT, and Markdown.<br>- Standardize text extraction pipeline.<br>- Ensure compatibility with FAISS-based chunking.                  | `langchain_community.document_loaders`, `unstructured`, `python-docx`, `markdown`               | Unified ingestion pipeline that can process diverse file formats. |
| **Phase 2** | Google Drive Integration      | Allow reading and indexing of enterprise documents directly from Google Drive.  | - Connect with Google Drive API.<br>- Add OAuth authentication.<br>- Support file listing and selective indexing.                                                 | Google Drive API, `google-auth`, `google-api-python-client`                                     | Secure integration for cloud document ingestion.                  |
| **Phase 3** | Folder-based Auto Ingestion   | Automate local document ingestion by watching folders for new or updated files. | - Implement folder monitoring using `watchdog`.<br>- Trigger parsing and indexing on change.<br>- Maintain indexing logs for updates.                             | `watchdog`, `os`, `langchain`, FAISS                                                            | Seamless background ingestion pipeline for local documents.       |
| **Phase 4** | Evaluation Framework          | Quantitatively evaluate RAG system before optimization.                         | - Integrate RAGAS for answer quality evaluation.<br>- Use LangSmith for trace-level monitoring.<br>- Record evaluation metrics (faithfulness, relevance).         | `RAGAS`, `LangSmith`, `langchain.evaluation`                                                    | Baseline performance report for retrieval and generation.         |
| **Phase 5** | Search Optimization           | Improve retrieval quality and ranking for context passages.                     | - Implement hybrid search (semantic + lexical).<br>- Integrate BM25 keyword search.<br>- Add reranking with cross-encoder models.<br>- Tune retrieval thresholds. | FAISS, BM25, `sentence-transformers`, `langchain.retrievers.multi_vector`, `colbert` (optional) | Significantly improved retrieval accuracy and context relevance.  |
| **Phase 6** | Caching and Reindexing        | Introduce cache mechanisms and efficient reindexing workflows.                  | - Add Redis or local cache for embeddings.<br>- Automate index refresh when documents change.<br>- Handle stale embeddings gracefully.                            | `Redis`, FAISS, `pickle`, file metadata tracking                                                | Reduced latency and stable index refresh workflow.                |
| **Phase 7** | Observability and Logging     | Enable visibility into pipeline execution and debugging.                        | - Add FastAPI request tracing and timing logs.<br>- Integrate LangSmith observability.<br>- Structured logging with log levels.                                   | `LangSmith`, `structlog`, `FastAPI` middlewares                                                 | Full runtime observability and traceable workflow history.        |
| **Phase 8** | Frontend Development          | Build interactive UI for end users.                                             | - Develop desktop UI with PySide6.<br>- Bind UI actions to FastAPI endpoints.<br>- Display chat interface, upload panel, and RAG responses.                       | **PySide6 (Qt for Python)**, FastAPI, optional Flask or React frontend                          | Intuitive interface for interacting with the assistant locally.   |

## License

This project is proprietary and intended for internal use only.

## Milestones

Planned milestones grouping phases into deliverable-focused releases:

| **Milestone**   | **Included Phases** | **Theme**                                    | **Deliverable**                                                                               |
| --------------- | ------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Milestone 1** | Phases 1 – 3        | **Document Ingestion & Indexing Automation** | Unified ingestion system supporting multiple file types, Google Drive, and folder auto-watch. |
| **Milestone 2** | Phase 4             | **Evaluation Framework**                     | Baseline RAG performance metrics and LangSmith integration.                                   |
| **Milestone 3** | Phase 5             | **Search Optimization**                      | Hybrid search, BM25, and reranking implemented.                                               |
| **Milestone 4** | Phase 6             | **Caching & Reindexing**                     | Embedding cache, incremental reindexing, and update tracking.                                 |
| **Milestone 5** | Phase 7             | **Observability & Logging**                  | LangSmith and structured FastAPI observability layer.                                         |
| **Milestone 6** | Phase 8             | **Frontend UI**                              | PySide6-based Windows application connected to backend API.                                   |

```
