from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

DATA_DIR = Path("data/docs")

def ingest_documents():
    documents = []
    
    for file in DATA_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        documents.append(text)
        
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 250,
        chunk_overlap = 50
    )
    
    chunks = splitter.create_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    vector_store.save_local("vectorstore")
    
    return len(chunks)