from pydantic import BaseModel, Field
from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.prompts import PromptTemplate

class AnswerGrade(BaseModel):
    """Binary score for answer quality check."""
    answer_score: str = Field(
        description="Must be 'yes' if the answer correctly answers the question, otherwise 'no'.",
        pattern="^(yes|no)$"
    )

def answer_grader(state: AgentState):
    question = state["query"]
    answer = state["answer"]

    llm_with_structured_output = llm.with_structured_output(AnswerGrade)

    prompt = PromptTemplate(
        template="""You are a strict answer grader.
        Question: {question}
        Answer: {answer}

        Determine if the answer fully and correctly addresses the question.
        If yes, return 'yes'. If not or partially, return 'no'.""",
        input_variables=["question", "answer"],
    )

    chain = prompt | llm_with_structured_output
    result = chain.invoke({"question": question, "answer": answer})

    return {"answer_score": result.answer_score}

