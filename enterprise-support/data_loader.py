from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os

def load_knowledge_base(product_name):
    loader = DirectoryLoader(f"./knowledge_bases/{product_name}", glob="**/*.md")
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=f"./chroma_db/{product_name}"
    )
    return vectorstore