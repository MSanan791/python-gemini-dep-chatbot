import os
from dotenv import load_dotenv

# Updated imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def load_and_embed_pdf(pdf_path=r"D:\Summer 2nd Year\mental_health_bot\mental_health_bot\data\MentalHealthSummary.pdf"):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split()

    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectordb = FAISS.from_documents(docs, embedding)
    vectordb.save_local("faiss_index")
    return vectordb

def load_vectorstore():
    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    return FAISS.load_local(
        "faiss_index",
        embedding,
        allow_dangerous_deserialization=True
    )
