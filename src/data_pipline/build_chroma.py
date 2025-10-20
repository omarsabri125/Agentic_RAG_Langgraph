from .loader import load_data
from .textsplitter import split_documents
from .embeddings import get_embeddings
from langchain_community.vectorstores import Chroma
import os

def build_chroma_from_urls(urls: list[str]):

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    persist_directory = os.path.join(base_dir, "data", "chroma_db")
    os.makedirs(persist_directory, exist_ok=True)


    print("Loading data...")
    docs = load_data(urls)

    print("Splitting documents...")
    chunks = split_documents(docs)

    print("Generating embeddings...")
    embedding_model = get_embeddings()

    print("Building ChromaDB...")
    db = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=persist_directory)

    print(f"ChromaDB saved successfully at: {persist_directory}")
    return db

if __name__ == "__main__":
    
    urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/"
   ]
    
    db = build_chroma_from_urls(urls)
    print("saved successfully")


