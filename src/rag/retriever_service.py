import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.chat_models import init_chat_model
# from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.output_parsers import StrOutputParser
from src.vectorstore.vector_service import load_vectorstore

load_dotenv()

def build_qa_prompt(context: str, query: str):
    """Builds RAG prompt using FAISS and Gemini 2.5 Flash."""
    prompt_template = ChatPromptTemplate(
        messages=[
            (
                "system", 
                "You are an internal AI Knowledge Assistant. "
                "Use the provided context to answer the question concisely. "
                "If you cannot find the answer, say 'Answer not found in knowledge base.'\"\n\n"
                "Context: {context} \n\n"
            ),
            (
                "user", 
                "Query: {query}"
            )
        ]
    )
    prompt = prompt_template.invoke({"context": context, "query": query})
    return prompt

def query_knowledge_base(query: str):
    """Query documents using Gemini RAG pipeline."""
    vectorstore = load_vectorstore("iaka_index")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    
    docs = retriever.invoke(query)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = build_qa_prompt(context, query)
    response = llm.invoke(prompt)
    
    return {
        "answer": response.content, 
        "prompt": prompt, 
        "sources": [doc.metadata for doc in docs]
    }