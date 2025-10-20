from langchain_community.document_loaders import WebBaseLoader

def load_data(urls: list[str]):

    all_docs = []
    for url in urls:
        try:
            print(f"Loading data from: {url}")
            loader = WebBaseLoader(url)
            docs = loader.load()
            all_docs.extend(docs)
        except Exception as e:
            print(f"Failed to load {url}: {e}")
    return all_docs

