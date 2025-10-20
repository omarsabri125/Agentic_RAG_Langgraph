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

