# Enterprise AI Agent

An enterprise-style AI Agent system designed with:
- Stateful reasoning
- Tool invocation
- Retrieval-Augmented Generation (RAG)
- Anomaly detection

## Architecture Overview

User → API → Agent → Tool → Response

## AI Agent Flow

1. User submits a query
2. Agent reasons over the request
3. Agent selects an appropriate tool:
   - Document search (RAG)
   - Database query
   - Anomaly detection
4. Tool executes and returns results
5. Agent synthesizes the final answer

## Tech Stack
- FastAPI
- LangGraph
- LangChain
