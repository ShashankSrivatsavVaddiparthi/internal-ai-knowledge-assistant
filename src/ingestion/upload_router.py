from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
import os
from datetime import datetime

router = APIRouter(prefix="/upload", tags=["Ingestion"])

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    """Accepts file uploads and saves them to local storage."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(UPLOAD_DIR, f"{timestamp}_{file.filename}")

        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)
        
        return {
            "filename": file.filename, 
            "path": file_path, 
            "status": "uploaded successfully"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))