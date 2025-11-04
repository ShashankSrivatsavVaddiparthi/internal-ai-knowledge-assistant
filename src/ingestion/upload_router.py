from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
import os
from datetime import datetime
from src.parsing.parser_service import parse_document, clean_and_save
from src.vectorstore.vector_service import chunk_and_embed
from typing import List

router = APIRouter(prefix="/upload", tags=["Ingestion"])

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_document(files: List[UploadFile] = File(...)):
    """Upload, store, parse, and clean multiple documents."""
    responses = []
    for file in files:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(UPLOAD_DIR, f"{timestamp}_{file.filename}")

        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)

        docs = parse_document(file_path)
        processed_path = clean_and_save(docs)
        index_info = chunk_and_embed(docs)

        responses.append({
            "filename": file.filename,
            "path": file_path,
            "processed": processed_path,
            "chunks_created": index_info["chunks"],
            "index_saved_at": index_info["index_path"],
            "status": "parsed and indexed successfully"
        })
    return {"results": responses}
