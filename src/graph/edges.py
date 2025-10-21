from .state import AgentState

def route_decision(state: AgentState):
    route = state.get("route", "web_search")
    if route == "vectorstore":
        return {"next": "vectorstore"}
    return {"next": "web_search"}

def route_documents(state: AgentState):
    score = state.get("score", "no")
    if score == "yes":
        return {"next": "generate"}
    return {"next": "rewrite"}

def decide_to_generate_after_rewriting(state: AgentState):
    query = state["query"]
    if query == "question not relevant":
        return {"next": "context_mismatch"}
    return {"next": "retriever"}