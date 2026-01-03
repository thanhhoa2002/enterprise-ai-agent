from fastapi import APIRouter
from app.rag.ingest import ingest_documents
from app.rag.retriever import retrieve_context

router = APIRouter(prefix="/api")

@router.post("/agent/chat")
def agent_chat():
    return {
        "message": "AI Agent is not implemented yet"
    }
    
@router.post("/rag/ingest")
def ingest():
    count = ingest_documents()
    return {"chunks_ingested": count}

@router.post("/rag/query")
def query_rag(query: str):
    context = retrieve_context(query)
    return {
        "query": query,
        "context": context
    }