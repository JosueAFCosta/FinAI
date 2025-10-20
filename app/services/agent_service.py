from app.schemas.agent_schema import AgentQuery, AgentResponse
from app.agent.rag_pipeline import generate_answer

class AgentService:
    @staticmethod
    def process_query(query: AgentQuery) -> AgentResponse:
        """Processa a consulta do usuário via LangChain + RAG."""
        response = generate_answer(query.query)
        return AgentResponse(answer=str(response))
