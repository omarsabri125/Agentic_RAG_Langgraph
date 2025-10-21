from graph.state import AgentState
from utils.llm_provider import llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

def rewrite_agent(state: AgentState):
    user_question = state["query"]
    docs = state.get("documents", [])

    if not docs:
        return {"query": "question not relevant"}

    prompt = PromptTemplate(
        template="""You are a question re-writer that converts an input question into a better optimized version for vector store retrieval.  
        You are given both a question and a document.  

        - First, check if the question is relevant to the document by identifying a connection or relevance between them.  
        - If there is some relevancy, rewrite the question based on its semantic intent and the context of the document.  
        - If no relevance is found, simply return this single word: "question not relevant" (no extra text).

        ⚠️ IMPORTANT:
        - Return ONLY the rewritten question text.
        - Do NOT include explanations, reasoning, or phrases like "Rewritten question:".
        - Do NOT include punctuation outside the question itself.

        Here is the user question:
        {question}

        Here is the retrieved document:
        {context}
        """,
        input_variables=["context", "question"],
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "context": docs,
        "question": user_question
    })

    better_query = response.strip()

    return {"query": better_query}
