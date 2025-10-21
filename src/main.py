from fastapi import FastAPI
from src.ingestion.upload_router import router as upload_router

app = FastAPI(title="Internal AI Knowledge Assistant")

app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "IAKA ingestion API is live."}