from typing import TypedDict

class AgentState(TypedDict):
    query: str
    documents: str
    answer: str
    route: str
    score: str
    grounded: str
    answer_score: str

