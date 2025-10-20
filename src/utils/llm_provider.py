from langchain_groq import ChatGroq
import os

llm = ChatGroq(model_name="llama-3.3-70b-versatile",
               api_key=os.getenv("GROQ_API_KEY"))
