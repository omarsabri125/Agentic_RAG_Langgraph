from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

def generate_answer(state: AgentState):
  query = state["query"]
  documents = state["documents"]

  prompt = PromptTemplate.from_template("""
  You are an assistant for question-answering tasks. 
  Use the following pieces of retrieved context to answer the question. 
  If you don't know the answer, just say that you don't know. 
  Use three sentences maximum and keep the answer concise.

  Question: {question}
  Context: {context}
  Answer:
  """)

  rag_chain = prompt | llm | StrOutputParser()

  response = rag_chain.invoke({
      "context": documents,
      "question": query
  })
  return {"answer": response}