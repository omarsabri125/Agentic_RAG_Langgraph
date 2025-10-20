from graph.state import AgentState
from langchain_community.tools.tavily_search import TavilySearchResults
import os

def search_agent(state: AgentState):
  query = state["query"]
  tool_instance = TavilySearchResults(k=3, tavily_api_key = os.getenv("TAVILY_API_KEY"))
  results = tool_instance.run(query)

  if isinstance(results, list):
    formatted_results = []
    for item in results:
      content = item.get("content","No content")
      formatted_results.append(content)


  documents = "\n\n".join(formatted_results)
  return {"documents": documents}