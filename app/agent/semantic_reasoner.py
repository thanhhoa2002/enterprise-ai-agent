from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

BUSINESS_TOPICS = [
    "company working policy",
    "remote work policy",
    "annual leave policy",
    "sick leave policy",
    "termination notice period",
    "information security policy"
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

TOPIC_VECTORS = embeddings.embed_documents(BUSINESS_TOPICS)

def semantic_need_rag(query: str, threshold: float = 0.35) -> bool:
    query_vector = embeddings.embed_query(query)
    
    similarities = cosine_similarity(
        [query_vector],
        TOPIC_VECTORS
    )[0]
    
    return np.max(similarities) > threshold