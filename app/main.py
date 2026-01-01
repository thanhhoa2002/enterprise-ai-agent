from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title= "Enterprise AI Agent",
    description="Enterprise AI Agent with RAG and Anomaly Detection",
    version="0.1.0"
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}