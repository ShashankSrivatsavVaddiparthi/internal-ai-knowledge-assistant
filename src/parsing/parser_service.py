import os
from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredFileLoader
from langchain_core.documents import Document
from typing import List

def parse_document(file_path: str) -> List[Document]:
    """Parses a single uploaded document into LangChain Document objects."""
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load()
    
    return docs

def clean_and_save(docs: List[Document], output_dir: str = "data/processed") -> str:
    """Cleans and saves extracted text to processed folder."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(
        output_dir, 
        os.path.basename(docs[0].metadata.get("source", "processed")) + ".txt"
    )
    with open(output_path, "w", encoding="utf-8") as f:
        for d in docs:
            clean_text = d.page_content.strip().replace("\n", " ").replace("  ", " ")
            f.write(clean_text + "\n")
    
    return output_path

