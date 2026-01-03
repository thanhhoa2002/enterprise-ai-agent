from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def retrieve_context(query: str, k: int = 3) -> str:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    docs = vectorstore.similarity_search(query, k=k)
    
    return "\n".join([doc.page_content for doc in docs])