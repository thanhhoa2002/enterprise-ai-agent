from re import A
from langgraph.graph import StateGraph
from app.agent.state import AgentState

def build_agent_graph():
    graph = StateGraph(AgentState)
    
    return graph