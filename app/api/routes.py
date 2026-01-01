from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.post("/agent/chat")
def agent_chat():
    return {
        "message": "AI Agent is not implemented yet"
    }