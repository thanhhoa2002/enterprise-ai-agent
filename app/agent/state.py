from typing import Optional, Dict
from pydantic import BaseModel

class AgentState(BaseModel):
    user_query: str
    context: Optional[Dict] = None
    tool_output: Optional[Dict] = None
    final_answer: Optional[str] = None