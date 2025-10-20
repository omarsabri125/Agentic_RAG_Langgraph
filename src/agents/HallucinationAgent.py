from pydantic import BaseModel, Field
from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.prompts import PromptTemplate

class HallucinationCheck(BaseModel):
    """Binary decision if answer is grounded in documents."""
    grounded: str = Field(
        description="Must be 'yes' if the answer is supported by the documents, or 'no' if it contains hallucinations.",
        pattern="^(yes|no)$"
    )

def hallucination_agent(state: AgentState):
    answer = state["answer"]
    docs = state["documents"]

    llm_with_structured_output = llm.with_structured_output(HallucinationCheck)

    prompt = PromptTemplate(
        template="""You are an evaluator checking if an answer is *semantically grounded* in a set of reference documents.

        You are given:
        - Generated Answer: {answer}
        - Reference Documents: {context}

        Determine if the answer is supported by the information in the documents.
        - Reply with only one word: "yes" or "no"
        """,
        input_variables=["answer", "context"],
    )
    chain = prompt | llm_with_structured_output

    response = chain.invoke({
        "answer": answer,
        "context": docs
    })

    grounded = response.grounded
    return {"grounded": grounded, "answer": answer}
