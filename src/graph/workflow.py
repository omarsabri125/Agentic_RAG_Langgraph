from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .edges import route_decision, route_documents
from agents import (router_agent, search_agent, generate_answer, 
                    retriever_agent, grade_agent, rewrite_agent, answer_grader, hallucination_agent)


def create_workflow():
    graph = StateGraph(AgentState)
    graph.add_node("RouterAgent", router_agent)
    graph.add_node("RouteDecision", route_decision)
    graph.add_node("SearchAgent", search_agent)
    graph.add_node("GenerateAnswer", generate_answer)
    graph.add_node("RetrieverAgent", retriever_agent)
    graph.add_node("GradeAgent", grade_agent)
    graph.add_node("RewriteAgent", rewrite_agent)
    graph.add_node("RouteDocuments", route_documents)
    graph.add_node("AnswerGrader", answer_grader)
    graph.add_node("HallucinationAgent", hallucination_agent)

    graph.add_edge(START, "RouterAgent")
    graph.add_edge("RouterAgent", "RouteDecision")
    graph.add_edge("SearchAgent", "GenerateAnswer")
    graph.add_edge("RetrieverAgent", "GradeAgent")
    graph.add_edge("GradeAgent", "RouteDocuments")
    graph.add_edge("GenerateAnswer", "AnswerGrader")

    graph.add_conditional_edges(
        "RouteDecision",
        lambda state: state.get("next"),
        {"vectorstore": "RetrieverAgent", "web_search": "SearchAgent"}
    )
    graph.add_conditional_edges(
        "RouteDocuments",
        lambda state: state.get("next"),
        {"generate": "GenerateAnswer", "rewrite": "RewriteAgent"}
    )
    graph.add_edge("RewriteAgent", "RetrieverAgent")

    graph.add_conditional_edges(
        "AnswerGrader",
        lambda state: state.get("answer_score"),
        {"yes": "HallucinationAgent", "no": "GenerateAnswer"}
    )
    graph.add_conditional_edges(
        "HallucinationAgent",
        lambda state: state.get("grounded"),
        {"yes": END, "no": "GenerateAnswer"}
    )

    app = graph.compile()

    return app

