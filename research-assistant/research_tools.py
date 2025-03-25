from langchain.document_loaders import ArxivLoader, PubMedLoader

def search_arxiv(query: str, max_results=5):
    return ArxivLoader(query=query, max_results=max_results).load()

def search_pubmed(query: str, max_results=5):
    return PubMedLoader(query=query, max_results=max_results).load()