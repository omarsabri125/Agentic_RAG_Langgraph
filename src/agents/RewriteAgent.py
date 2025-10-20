from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.messages import HumanMessage

def rewrite_agent(state: AgentState):

    user_question = state["query"]
    messages = [
        HumanMessage(
            content=f"""
            You are a helpful assistant that improves clarity of user questions.

            Rewrite the following question to make it clearer, grammatically correct, and semantically precise.
            Do NOT include any extra words like "Improved question:", "Rewritten:", or quotes — return ONLY the rewritten question text.

            Original question:
            -------
            {user_question}
            -------
            """
        )
    ]

    llm_response = llm.invoke(messages)
    better_query = llm_response.content.strip()
    return {"query": better_query}