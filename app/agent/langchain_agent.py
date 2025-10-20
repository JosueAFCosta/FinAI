"""
Configuração do agente LangChain com o modelo OpenAI.
"""
from langchain_openai import ChatOpenAI
from app.config import settings

def get_openai_agent():
    """
    Inicializa o agente OpenAI via LangChain.
    """
    return ChatOpenAI(
        model="gpt-4o-mini",  # pode trocar pra gpt-4o, gpt-4-turbo, etc
        temperature=0.3,
        openai_api_key=settings.OPENAI_API_KEY
    )
