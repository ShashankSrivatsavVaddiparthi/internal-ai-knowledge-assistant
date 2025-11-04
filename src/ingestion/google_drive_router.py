from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from src.vectorstore.vector_service import chunk_and_embed
from langchain_googledrive.document_loaders import GoogleDriveLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_core.documents import Document
from typing import List
import os
import traceback

credentials = "google_drive_tokens/credentials.json"

google_drive_file_router = APIRouter(prefix="/google-drive-file", tags=["Google Drive"])
google_drive_folder_router = APIRouter(prefix="/google-drive-folder", tags=["Google Drive"])

PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def get_filename_from_metadata(doc: Document) -> str:
    """Extract filename from Google Drive document metadata, removing spaces."""
    # Google Drive files typically have "title" in metadata
    title = doc.metadata.get("title", "gdrive_file")
    # Remove spaces and replace with underscores, and remove any invalid characters
    filename = title.replace(" ", "_").replace("/", "_").replace("\\", "_")
    # Remove any other problematic characters
    filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))
    return filename

def clean_and_save_gdrive(docs: List[Document], output_dir: str = "data/processed") -> List[str]:
    """Cleans and saves Google Drive documents, each with its own filename from metadata."""
    os.makedirs(output_dir, exist_ok=True)
    
    if not docs:
        return []
    
    processed_paths = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Process each document individually with its own filename
    for idx, doc in enumerate(docs):
        filename = get_filename_from_metadata(doc)
        
        # Add index to filename if there are multiple documents to avoid conflicts
        if len(docs) > 1:
            output_path = os.path.join(output_dir, f"{timestamp}_{filename}_{idx}.txt")
        else:
            output_path = os.path.join(output_dir, f"{timestamp}_{filename}.txt")
        
        with open(output_path, "w", encoding="utf-8") as f:
            clean_text = doc.page_content.strip().replace("\n", " ").replace("  ", " ")
            f.write(clean_text + "\n")
        
        processed_paths.append(output_path)
    
    return processed_paths

@google_drive_file_router.post("/")
async def upload_google_drive_file(file_id: str = Query(..., description="Google Drive file ID")):
    """Upload, parse, and clean a file from Google Drive."""
    try:
        # Check if credentials file exists
        if not os.path.exists(credentials):
            raise HTTPException(
                status_code=400, 
                detail=f"Google Drive credentials file not found at {credentials}. Please ensure credentials.json exists."
            )
        
        # Set environment variable for GoogleDriveLoader to use
        os.environ["GOOGLE_ACCOUNT_FILE"] = credentials
        
        loader = GoogleDriveLoader(
            file_ids=[file_id], 
            conv_mapping={
                "application/pdf": UnstructuredFileLoader
            }, 
        )
        docs = loader.load()
        
        if not docs:
            raise HTTPException(status_code=404, detail="No documents found for the given file ID")
        
        # Process each document individually using custom function for Google Drive
        processed_paths = clean_and_save_gdrive(docs, output_dir=PROCESSED_DIR)
        index_info = chunk_and_embed(docs)
        
        # Get file titles from metadata
        file_titles = [doc.metadata.get("title", file_id) for doc in docs]
        
        return {
            "message": f"Processed {len(docs)} document(s) and indexed ({index_info['chunks']} chunks)",
            "filenames": file_titles,
            "processed_paths": processed_paths,
            "chunks_created": index_info["chunks"],
            "index_saved_at": index_info["index_path"],
            "status": "parsed and indexed successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        # Include full traceback for debugging
        error_detail = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)

@google_drive_folder_router.post("/")
async def upload_google_drive_folder(folder_id: str = Query(..., description="Google Drive folder ID")):
    """Upload, parse, and clean all files from a Google Drive folder."""
    try:
        # Check if credentials file exists
        if not os.path.exists(credentials):
            raise HTTPException(
                status_code=400, 
                detail=f"Google Drive credentials file not found at {credentials}. Please ensure credentials.json exists."
            )
        
        # Set environment variable for GoogleDriveLoader to use
        os.environ["GOOGLE_ACCOUNT_FILE"] = credentials
        
        loader = GoogleDriveLoader(
            folder_id=folder_id,
            conv_mapping={
                "application/pdf": UnstructuredFileLoader, 
            },
            recursive=False,
        )
        docs = loader.load()
        
        if not docs:
            raise HTTPException(status_code=404, detail="No documents found in the given folder ID")
        
        # Process each document individually using custom function for Google Drive
        processed_paths = clean_and_save_gdrive(docs, output_dir=PROCESSED_DIR)
        index_info = chunk_and_embed(docs)
        
        # Get file titles from metadata
        file_titles = [doc.metadata.get("title", folder_id) for doc in docs]
        
        return {
            "message": f"Processed {len(docs)} document(s) from folder and indexed ({index_info['chunks']} chunks)",
            "filenames": file_titles,
            "processed_paths": processed_paths,
            "chunks_created": index_info["chunks"],
            "index_saved_at": index_info["index_path"],
            "status": "parsed and indexed successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        # Include full traceback for debugging
        error_detail = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)

