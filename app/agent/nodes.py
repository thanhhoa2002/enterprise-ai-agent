from app.rag.retriever import retrieve_context
from app.agent.semantic_reasoner import semantic_need_rag

def reason_node(state):
    state.need_rag = semantic_need_rag(state.user_query)
    return state

def rag_node(state):
    if state.need_rag:
        state.context = retrieve_context(state.user_query)
    return state

def final_node(state):
    if state.context:
        state.final_answer = (
            f"Based on internal documents:\n{state.context}"
        )
    else:
        state.final_answer = (
            "This is a general question; there's no need to access an internal document."
        )
    return state