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

See the detailed plan in [`ROADMAP.md`](./ROADMAP.md). TL;DR milestones:

- M1 (P1–P3): Core Document Intelligence — multi-format ingestion, better chunking, folder ingest
- M2 (P4): Automation & Sync — real-time folder monitoring and auto re-indexing
- M3 (P5): Evaluation & Quality — baseline RAG metrics with RAGAS + LangSmith
- M4 (P6): Search Optimization — hybrid (semantic+BM25) and reranking
- M5 (P7): Caching & Reindexing — faster retrieval, incremental refresh
- M6 (P8): Observability & Tracing — logging, tracing, performance tracking
- M7 (P9): Frontend Integration — PySide6 or web UI over FastAPI


## License

This project is proprietary and intended for internal use only.

```

```
