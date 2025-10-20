def formatted_documents(documents):
    return "\n\n".join(doc.page_content for doc in documents)