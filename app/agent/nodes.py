from turtle import st
from app.rag.retriever import retrieve_context
from app.agent.semantic_reasoner import semantic_need_rag
from app.agent.llm_generator import generate_answer

def reason_node(state):
    state.need_rag = semantic_need_rag(state.user_query)
    return state

def rag_node(state):
    if state.need_rag:
        state.context = retrieve_context(state.user_query)
    return state

def final_node(state):
    state.final_answer = generate_answer(
        query = state.user_query,
        context = state.context
    )
    return state