# Project Roadmap

_Last updated: November 4, 2025_

This document outlines the planned development phases and milestones for the Internal AI Knowledge Assistant project.

---

## TL;DR: Phase Overview

| **Phase** | **Title**                         | **Objective / Focus**                                                                            |
| --------- | --------------------------------- | ------------------------------------------------------------------------------------------------ |
| P1        | Multi-Format Document Loader      | Add support for `.docx`, `.md`, `.txt`, and other structured documents in addition to PDFs.      |
| P2        | Enhanced Chunking & Indexing      | Refine document splitting logic and indexing workflow for consistent retrieval quality.          |
| P3        | Folder-Based Ingestion            | Enable the system to read all documents inside a given folder path and index them automatically. |
| P4        | Real-Time Folder Monitoring       | Watch specified folders for new or updated files and trigger ingestion automatically.            |
| P5        | Evaluation & Quality Benchmarking | Evaluate baseline RAG performance before search optimization.                                    |
| P6        | Search Optimization & Reranking   | Implement hybrid (semantic + keyword) search and add reranking for better retrieval.             |
| P7        | Caching & Reindexing Efficiency   | Improve retrieval speed and manage reindexing intelligently.                                     |
| P8        | Observability & Tracing           | Add system-level monitoring, logging, and performance tracking.                                  |
| P9        | Frontend Integration & Access     | Create an enterprise-grade user interface (Windows or web) to interact with FastAPI.             |

## Milestones

| **Milestone** | **Included Phases** | **Title**                             | **Objective / Focus**                                                                 | **Expected Outcome**                                              |
| ------------- | ------------------- | ------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| M1            | P1 – P3             | Core Document Intelligence            | Build ingestion and indexing foundation across multiple file types and local folders. | Robust RAG pipeline with multi-format and folder-based ingestion. |
| M2            | P4                  | Automation & Sync                     | Implement real-time folder monitoring for automatic re-indexing.                      | Dynamic ingestion pipeline that updates automatically.            |
| M3            | P5                  | Evaluation & Quality Benchmarking     | Benchmark system accuracy, latency, and relevance.                                    | Baseline metrics established for further optimization.            |
| M4            | P6                  | Search Optimization & Reranking       | Integrate hybrid search and reranking.                                                | Enhanced retrieval performance and contextual accuracy.           |
| M5            | P7                  | Caching & Reindexing Efficiency       | Optimize speed and reindexing strategy.                                               | Faster, scalable retrieval and refresh workflows.                 |
| M6            | P8                  | Observability & Tracing               | Add monitoring, logging, and tracing.                                                 | Transparent performance insights and diagnostics.                 |
| M7            | P9                  | Frontend Integration & Access         | Build final user interface (Windows app or web).                                      | Complete, enterprise-ready assistant experience.                  |

---

## Development Phases

### P1: Multi-Format Document Loader
**Objective:** Expand ingestion to handle DOCX, Markdown, TXT, and other structured files beyond PDFs.
**Core Tasks:**
- Integrate `langchain.document_loaders` and custom loaders where needed
- Standardize text extraction and metadata normalization
- Ensure compatibility with current FAISS indexing flow
**Key Tools:** `langchain.document_loaders`, `unstructured`, `python-docx`, `markdown`
**Expected Outcome:** Broader ingestion capability for diverse internal files

### P2: Enhanced Chunking & Indexing
**Objective:** Improve chunk split logic and indexing consistency for higher-quality retrieval.
**Core Tasks:**
- Adopt `RecursiveCharacterTextSplitter` with format-aware heuristics
- Normalize chunk metadata and IDs
- Rebuild FAISS indexes with tuned embedding settings
**Key Tools:** `RecursiveCharacterTextSplitter`, `FAISS`, `sentence-transformers`
**Expected Outcome:** Cleaner chunks and better embeddings for retrieval quality

### P3: Folder-Based Ingestion
**Objective:** Index all documents within a specified local directory path.
**Core Tasks:**
- Recursively traverse directories with allow/deny globs
- Batch load and index supported file types
- Maintain per-file indexing status
**Key Tools:** `os`, `pathlib`, `langchain`, `FAISS`
**Expected Outcome:** Seamless ingestion of multiple local files via directory path

### P4: Real-Time Folder Monitoring
**Objective:** Continuously watch folders and auto-trigger ingestion on changes.
**Core Tasks:**
- Implement watchers with `watchdog`
- Debounce rapid change events and coalesce batches
- Trigger incremental reindexing for new/updated files
**Key Tools:** `watchdog`, `os`, `langchain`
**Expected Outcome:** Continuous, automated updates to the local document index

### P5: Evaluation & Quality Benchmarking
**Objective:** Establish baseline RAG quality and latency metrics before optimization.
**Core Tasks:**
- Integrate `RAGAS` for faithfulness/relevance
- Use `LangSmith` traces for pipeline observability during eval runs
- Persist and compare baseline metrics over time
**Key Tools:** `RAGAS`, `LangSmith`
**Expected Outcome:** Baseline metrics to guide further optimization

### P6: Search Optimization & Reranking
**Objective:** Improve recall and precision with hybrid search and reranking.
**Core Tasks:**
- Add BM25 lexical search and combine with semantic retrieval
- Introduce rerankers (e.g., cross-encoders) for top-K passages
- Tune thresholds and weights for hybrid scorer
**Key Tools:** `BM25`, hybrid retrievers, rerankers, `FAISS`, `sentence-transformers`
**Expected Outcome:** Higher recall and contextual precision

### P7: Caching & Reindexing Efficiency
**Objective:** Reduce latency and optimize refresh cycles.
**Core Tasks:**
- Embed-level caching (local/Redis) to avoid recomputation
- Incremental indexing keyed by file hash/mtime
- Prune stale entries safely
**Key Tools:** Local cache, `Redis` (optional), incremental indexing logic
**Expected Outcome:** Lower latency and optimized refresh cycles

### P8: Observability & Tracing
**Objective:** Provide system-level monitoring and visibility.
**Core Tasks:**
- Add structured logging and timing around critical paths
- Integrate `LangSmith` for tracing
- Dashboard key pipeline metrics
**Key Tools:** `LangSmith`, logging middleware
**Expected Outcome:** Clear visibility into pipeline health and metrics

### P9: Frontend Integration & Access
**Objective:** Deliver a usable enterprise UI tied to FastAPI.
**Core Tasks:**
- Build Windows desktop app with `PySide6` or a web frontend
- Wire UI actions to backend ingestion/query endpoints
- Provide chat, upload, and results visualization
**Key Tools:** `PySide6` / web frontend, FastAPI
**Expected Outcome:** Usable and deployable enterprise interface

---

For questions or suggestions, open an issue or contact the maintainer.
