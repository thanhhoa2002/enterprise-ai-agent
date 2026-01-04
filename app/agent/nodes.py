from app.rag.retriever import retrieve_context

def reason_node(state):
    query = state.user_query.lower()
    
    keywords = [
        "policy",
        "leave",
        "remote",
        "termination",
        "working",
        "security"
    ]
    
    state.need_rag = any(k in query for k in keywords)
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