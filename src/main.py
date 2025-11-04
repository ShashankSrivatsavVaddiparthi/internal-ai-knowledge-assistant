from fastapi import FastAPI, Query
from src.ingestion.upload_router import router as upload_router
from src.rag.retriever_service import query_knowledge_base
from src.ingestion.google_drive_router import google_drive_file_router, google_drive_folder_router
from src.ingestion.local_folder_router import local_folder_router

app = FastAPI(title="Internal AI Knowledge Assistant")
app.include_router(upload_router)
app.include_router(google_drive_file_router)
app.include_router(google_drive_folder_router)
app.include_router(local_folder_router)

@app.get("/")
def root():
    return {"message": "IAKA ingestion API is live."}

@app.get("/ask/")
def ask(query: str = Query(..., description="Your question")):
    """Ask a question against the internal knowledge base."""
    response = query_knowledge_base(query)
    return response