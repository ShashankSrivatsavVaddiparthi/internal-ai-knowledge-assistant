import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.chat_models import init_chat_model
# from langchain.chains import create_retrieval_chain
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from src.vectorstore.vector_service import load_vectorstore

load_dotenv()

def build_qa_prompt():
    """Builds RAG chain using FAISS and Gemini 2.5 Flash."""
    # vectorstore = load_vectorstore("iaka_index")

    # llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    
    # retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    template = """
    You are an internal AI Knowledge Assistant. 
    Use the provided context to answer the question concisely. 
    If you cannot find the answer, say "Answer not found in knowledge base."
    
    Context: 
    {context} 

    Questions:
    {question}
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"], 
        template=template
    )

    # chain = RetrievalQA.from_chain_type(
    #     llm=llm, 
    #     retriever=retriever,
    #     return_source_documents=True, 
    #     chain_type_kwargs={"prompt": prompt}
    # )

    return prompt

def query_knowledge_base(query: str):
    """Query documents using Gemini RAG pipeline."""
    vectorstore = load_vectorstore("iaka_index")
    llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    prompt_template = build_qa_prompt()
    result = prompt_template.invoke({"context": retriever.invoke(query), "question": query})
    response = llm.invoke(result)
    return {
        "answer": response.content, 
        "prompt": result
        # "sources": [doc.metadata for doc in result["source_documents"]]
    }