from typing import Optional, Dict
from pydantic import BaseModel

class AgentState(BaseModel):
    user_query: str
    need_rag: Optional[bool] = None
    context: Optional[str] = None
    final_answer: Optional[str] = None