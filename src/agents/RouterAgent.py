from pydantic import BaseModel, Field
from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.messages import SystemMessage, HumanMessage

class RouteDecision(BaseModel):
    route: str = Field(
        ...,
        description= "\n".join([
            "Routing decision — must be either 'vectorstore' or 'web_search'. ",
            "'vectorstore' if the question can be answered from the internal knowledge base, ",
            "'web_search' otherwise.",
        ]),
        pattern="^(vectorstore|web_search)$"
    )

def router_agent(state: AgentState):
  query = state["query"]
  classifier_llm = llm.with_structured_output(RouteDecision)

  system_message = SystemMessage(
      content=(
            "You are a routing classifier that decides whether a user question "
            "should be answered using internal knowledge (vectorstore) or external "
            "information (web_search).\n\n"
            "Rules:\n"
            "- Use 'vectorstore' if the query can be answered from stored documents, prior context, or internal data.\n"
            "- Use 'web_search' if the query requires current events, general world knowledge, or information not in the internal data."
      )
  )
  human_message = HumanMessage(content=f"User question: {query}")
  messages = [system_message, human_message]

  output = classifier_llm.invoke(messages)
  return {"route": output.route}

