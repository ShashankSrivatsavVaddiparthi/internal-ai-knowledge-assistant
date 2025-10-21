from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
import os
from datetime import datetime
from src.parsing.parser_service import parse_document, clean_and_save

router = APIRouter(prefix="/upload", tags=["Ingestion"])

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    """Upload, store, parse, and clean a document."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(UPLOAD_DIR, f"{timestamp}_{file.filename}")

        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)
        
        docs = parse_document(file_path)
        processed_path = clean_and_save(docs)
        
        return {
            "filename": file.filename, 
            "path": file_path, 
            "processed": processed_path, 
            "status": "parsed and stored successfully"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))