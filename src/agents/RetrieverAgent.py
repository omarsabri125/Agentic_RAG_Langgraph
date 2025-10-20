from graph.state import AgentState
from utils.format_docs import formatted_documents
from langchain_community.vectorstores import Chroma
from data_pipline.embeddings import get_embeddings
import os
def retriever_agent(state: AgentState):
  
  query = state["query"]
  embedding_model = get_embeddings()
  base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  persist_directory = os.path.join(base_dir, "data", "chroma_db")
  vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )
  retriever = vectorstore.as_retriever()
  documents = retriever.invoke(query)
  documents = formatted_documents(documents)
  return {"documents": documents}