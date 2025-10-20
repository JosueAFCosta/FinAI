from fastapi import APIRouter
from app.schemas.agent_schema import AgentQuery, AgentResponse
from app.services.agent_service import AgentService

router = APIRouter(prefix="/agent", tags=["AI Agent"])

@router.post("/ask", response_model=AgentResponse)
def ask_agent(query: AgentQuery):
    """Permite o usuário fazer perguntas financeiras em linguagem natural."""
    return AgentService.process_query(query)
