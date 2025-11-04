from fastapi import APIRouter, HTTPException, Query
from typing import List
from pathlib import Path
import os

from src.parsing.parser_service import parse_document, clean_and_save
from src.vectorstore.vector_service import chunk_and_embed


local_folder_router = APIRouter(prefix="/local-folder", tags=["Local Files"])


SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".md", ".txt"}


def _iter_files(folder_path: Path, recursive: bool) -> List[Path]:
    if recursive:
        return [p for p in folder_path.rglob("*") if p.is_file()]
    return [p for p in folder_path.glob("*") if p.is_file()]


@local_folder_router.post("/")
def ingest_local_folder(
    path: str = Query(..., description="Absolute or relative folder path"),
    recursive: bool = Query(True, description="Recurse into subdirectories"),
    include_ext: List[str] | None = Query(None, description="Whitelist extensions, e.g. .pdf,.md"),
):
    """Parse, clean, and index all supported documents from a local folder."""
    folder_path = Path(path).expanduser().resolve() if not Path(path).is_absolute() else Path(path)

    if not folder_path.exists() or not folder_path.is_dir():
        raise HTTPException(status_code=400, detail=f"Folder path not found or not a directory: {path}")

    allowed_exts = {e.strip().lower() for e in include_ext} if include_ext else SUPPORTED_EXTENSIONS

    all_files = _iter_files(folder_path, recursive)
    candidate_files = [p for p in all_files if p.suffix.lower() in allowed_exts]

    if not candidate_files:
        return {"message": "No files matched criteria", "folder": str(folder_path), "count": 0}

    processed_paths: List[str] = []
    all_docs = []

    for file_path in candidate_files:
        try:
            docs = parse_document(str(file_path))
            processed_path = clean_and_save(docs)
            processed_paths.append(processed_path)
            all_docs.extend(docs)
        except Exception as e:
            # Skip problematic files but continue processing others
            processed_paths.append(f"ERROR: {file_path.name}: {e}")

    if not all_docs:
        raise HTTPException(status_code=500, detail="No documents were parsed successfully")

    index_info = chunk_and_embed(all_docs)

    return {
        "message": f"Processed {len(candidate_files)} file(s) and indexed ({index_info['chunks']} chunks)",
        "folder": str(folder_path),
        "processed_paths": processed_paths,
        "chunks_created": index_info["chunks"],
        "index_saved_at": index_info["index_path"],
        "status": "parsed and indexed successfully",
    }


