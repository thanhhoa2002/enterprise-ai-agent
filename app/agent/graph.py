from langgraph.graph import StateGraph
from app.agent.state import AgentState
from app.agent.nodes import reason_node, rag_node, final_node

def build_agent_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("reason", reason_node)
    graph.add_node("rag", rag_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("reason")
    
    graph.add_edge("reason", "rag")
    graph.add_edge("rag", "final")

    return graph.compile()