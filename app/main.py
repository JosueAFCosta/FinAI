from fastapi import FastAPI
from app.api import routes_transactions, routes_reports, routes_agent

app = FastAPI(
    title="Finance AI Agent",
    description="Agente de IA para controle financeiro usando RAG, LangChain e Gemini.",
    version="1.0.0"
)

# Inclui as rotas
app.include_router(routes_transactions.router)
app.include_router(routes_reports.router)
app.include_router(routes_agent.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "🚀 Finance AI Agent is running!"}
