from pydantic import BaseModel, Field
from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.prompts import PromptTemplate

class Grade(BaseModel):
    """
    Represents a binary relevance score for evaluating how relevant
    a document or response is.
    """

    binary_score: str = Field(
        description="Relevance score: must be exactly 'yes' (relevant) or 'no' (not relevant).",
        pattern="^(yes|no)$"
    )

def grade_agent(state: AgentState):
  user_question = state["query"]
  docs = state["documents"]
  llm_with_structured_output = llm.with_structured_output(Grade)

  # Prompt
  prompt = PromptTemplate(
        template="""You are a grader assessing relevance of a retrieved document to a user question. \n
        Here is the retrieved document: \n\n {context} \n\n
        Here is the user question: {question} \n
        If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
        input_variables=["context", "question"],
    )
  chain = prompt | llm_with_structured_output

  response = chain.invoke({
      "context": docs,
      "question": user_question
  })

  score = response.binary_score
  return {"score": score}
