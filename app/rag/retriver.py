from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever()

def search_knowledge(query):

    docs = retriever.invoke(query)

    return "\n".join([
        doc.page_content for doc in docs
    ])