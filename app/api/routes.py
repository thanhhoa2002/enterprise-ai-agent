from fastapi import APIRouter
from app.rag.ingest import ingest_documents
from app.rag.retriever import retrieve_context
from app.agent.graph import build_agent_graph
from app.agent.state import AgentState

router = APIRouter(prefix="/api")

agent = build_agent_graph()

@router.post("/agent/chat")
def agent_chat(query: str):
    state = AgentState(user_query=query)
    result = agent.invoke(state)
    return {
        "answer": result.get("final_answer")
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