import os
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List

VECTOR_DIR = "data/vectors"
os.makedirs(VECTOR_DIR, exist_ok=True)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def chunk_and_embed(docs: List[Document], index_name: str = "iaka_index"):
    """Splits documents into chunks, embeds them, and saves FAISS index."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)

    save_path = os.path.join(VECTOR_DIR, index_name)
    db.save_local(save_path)

    return {
        "chunks": len(chunks), 
        "index_path": save_path
    }

def load_vectorstore(index_name: str = "iaka_index"):
    """Loads FAISS index from local directory."""
    path = os.path.join(VECTOR_DIR, index_name)
    if not os.path.exists(path):
        raise FileNotFoundError("Vector index not found.")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)