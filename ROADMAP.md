# Project Roadmap

_Last updated: October 29, 2025_

This document outlines the planned development phases and milestones for the Internal AI Knowledge Assistant project. The current status is MVP (see Phase 0).

---

## TL;DR: Phase Overview

| **Phase**   | **Title**                     | **Goal / Objective**                                      |
| ----------- | ----------------------------- | --------------------------------------------------------- |
| Phase 0     | MVP                           | PDF ingestion, FAISS vector store, basic UI               |
| Phase 1     | Multi-format Document Loading  | Ingest DOCX, TXT, Markdown; standardize extraction        |
| Phase 2     | Google Drive Integration       | Ingest and index files from Google Drive                  |
| Phase 3     | Folder-based Auto Ingestion    | Watch folders for new/updated files, auto-index           |
| Phase 4     | Evaluation Framework           | RAG evaluation, LangSmith integration, metrics            |
| Phase 5     | Search Optimization            | Hybrid search, BM25, reranking, retrieval tuning          |
| Phase 6     | Caching and Reindexing         | Embedding cache, incremental reindexing                   |
| Phase 7     | Observability and Logging      | FastAPI tracing, LangSmith, structured logging            |
| Phase 8     | Frontend Development           | PySide6 desktop UI, chat/upload, connect to backend       |

## Milestones

| **Milestone**   | **Included Phases** | **Theme**                                    | **Deliverable**                                                                               |
| --------------- | ------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Milestone 1** | Phases 1 – 3        | **Document Ingestion & Indexing Automation** | Unified ingestion system supporting multiple file types, Google Drive, and folder auto-watch. |
| **Milestone 2** | Phase 4             | **Evaluation Framework**                     | Baseline RAG performance metrics and LangSmith integration.                                   |
| **Milestone 3** | Phase 5             | **Search Optimization**                      | Hybrid search, BM25, and reranking implemented.                                               |
| **Milestone 4** | Phase 6             | **Caching & Reindexing**                     | Embedding cache, incremental reindexing, and update tracking.                                 |
| **Milestone 5** | Phase 7             | **Observability & Logging**                  | LangSmith and structured FastAPI observability layer.                                         |
| **Milestone 6** | Phase 8             | **Frontend UI**                              | PySide6-based Windows application connected to backend API.                                   |

---

## Development Phases

### Phase 0: MVP
**Goal:** Baseline project (current state): PDF ingestion, FAISS vector store, basic UI.
**Core Tasks:**
- Handle PDF uploads and extraction
- Chunking & embeddings
- FAISS indexing
- Basic query endpoint and Gradio/FastAPI UI
**Key Tools:** `faiss-cpu`, `langchain`, `sentence-transformers`, `fastapi`, `gradio`, `pymupdf`, `unstructured`
**Expected Outcome:** Working MVP: PDF ingestion + semantic search + basic UI

### Phase 1: Multi-format Document Loading
**Goal:** Expand ingestion pipeline to handle multiple file types beyond PDFs.
**Core Tasks:**
- Integrate loaders for DOCX, TXT, and Markdown
- Standardize text extraction pipeline
- Ensure compatibility with FAISS-based chunking
**Key Tools:** `langchain_community.document_loaders`, `unstructured`, `python-docx`, `markdown`
**Expected Outcome:** Unified ingestion pipeline that can process diverse file formats

### Phase 2: Google Drive Integration
**Goal:** Allow reading and indexing of enterprise documents directly from Google Drive.
**Core Tasks:**
- Connect with Google Drive API
- Add OAuth authentication
- Support file listing and selective indexing
**Key Tools:** Google Drive API, `google-auth`, `google-api-python-client`
**Expected Outcome:** Secure integration for cloud document ingestion

### Phase 3: Folder-based Auto Ingestion
**Goal:** Automate local document ingestion by watching folders for new or updated files.
**Core Tasks:**
- Implement folder monitoring using `watchdog`
- Trigger parsing and indexing on change
- Maintain indexing logs for updates
**Key Tools:** `watchdog`, `os`, `langchain`, FAISS
**Expected Outcome:** Seamless background ingestion pipeline for local documents

### Phase 4: Evaluation Framework
**Goal:** Quantitatively evaluate RAG system before optimization.
**Core Tasks:**
- Integrate RAGAS for answer quality evaluation
- Use LangSmith for trace-level monitoring
- Record evaluation metrics (faithfulness, relevance)
**Key Tools:** `RAGAS`, `LangSmith`, `langchain.evaluation`
**Expected Outcome:** Baseline performance report for retrieval and generation

### Phase 5: Search Optimization
**Goal:** Improve retrieval quality and ranking for context passages.
**Core Tasks:**
- Implement hybrid search (semantic + lexical)
- Integrate BM25 keyword search
- Add reranking with cross-encoder models
- Tune retrieval thresholds
**Key Tools:** FAISS, BM25, `sentence-transformers`, `langchain.retrievers.multi_vector`, `colbert` (optional)
**Expected Outcome:** Significantly improved retrieval accuracy and context relevance

### Phase 6: Caching and Reindexing
**Goal:** Introduce cache mechanisms and efficient reindexing workflows.
**Core Tasks:**
- Add Redis or local cache for embeddings
- Automate index refresh when documents change
- Handle stale embeddings gracefully
**Key Tools:** `Redis`, FAISS, `pickle`, file metadata tracking
**Expected Outcome:** Reduced latency and stable index refresh workflow

### Phase 7: Observability and Logging
**Goal:** Enable visibility into pipeline execution and debugging.
**Core Tasks:**
- Add FastAPI request tracing and timing logs
- Integrate LangSmith observability
- Structured logging with log levels
**Key Tools:** `LangSmith`, `structlog`, `FastAPI` middlewares
**Expected Outcome:** Full runtime observability and traceable workflow history

### Phase 8: Frontend Development
**Goal:** Build interactive UI for end users.
**Core Tasks:**
- Develop desktop UI with PySide6
- Bind UI actions to FastAPI endpoints
- Display chat interface, upload panel, and RAG responses
**Key Tools:** **PySide6 (Qt for Python)**, FastAPI, optional Flask or React frontend
**Expected Outcome:** Intuitive interface for interacting with the assistant locally

---

For questions or suggestions, open an issue or contact the maintainer.
