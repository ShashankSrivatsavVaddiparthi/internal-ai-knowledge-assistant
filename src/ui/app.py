import os
import gradio as gr
import aiofiles
import requests
from datetime import datetime
from src.rag.retriever_service import query_knowledge_base
from src.ingestion.upload_router import upload_document
from src.parsing.parser_service import parse_document, clean_and_save
from src.vectorstore.vector_service import chunk_and_embed

def ask_iaka(question):
    """Handle gradio input."""
    result = query_knowledge_base(question)
    return result["answer"]

# UPLOAD_DIR = "data/uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# def handle_upload(files):
#     """Gradio-compatible synchronous upload handler."""
#     if not files:
#         return "No files uploaded."
#     results = []
#     for file in files:
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{timestamp}_{file.name}"
#         dest_path = os.path.join(UPLOAD_DIR, filename)
#         with open(dest_path, "wb") as f:
#             f.write(file.read())

#         # Process document
#         docs = parse_document(dest_path)
#         processed_path = clean_and_save(docs)
#         index_info = chunk_and_embed(docs)

#         results.append(f"{file.name}: parsed and indexed ({index_info['chunks']} chunks)")
#     return "\n".join(results)

with gr.Blocks(title="iAKA - Internal AI Knowledge Assistant") as demo:
    gr.Markdown("# iAKA - Internal AI Knowledge Assistant")
    gr.Markdown("Ask questions about your internal documents.")
    
    with gr.Tab("Ask Questions"):
        question = gr.Textbox(label="Enter your question", lines=2)
        with gr.Row():
            answer = gr.Textbox(label="Answer", interactive=False)
            # context = gr.Textbox(label="Context used", interactive=False)
            # sources = gr.JSON(label="Source metadata")
        submit = gr.Button("Ask")
        submit.click(ask_iaka, inputs=[question], outputs=[answer])

    # with gr.Tab("Upload Documents"):
    #     uploader = gr.File(label="Upload a document", file_count="multiple")
    #     upload_btn = gr.Button("Upload")
    #     upload_output = gr.Textbox(label="Upload Status", interactive=False)
    #     upload_btn.click(handle_upload, inputs=[uploader], outputs=[upload_output])


demo.launch()