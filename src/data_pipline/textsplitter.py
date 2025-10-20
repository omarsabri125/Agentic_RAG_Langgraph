from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=500, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    return chunks