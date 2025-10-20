"""
Pipeline completo de RAG: busca dados + gera resposta com base no contexto.
"""
from app.agent.retriever import retrieve_relevant_data
from app.agent.langchain_agent import get_openai_agent
from app.agent.prompts import SYSTEM_PROMPT

def generate_answer(query: str):
    """
    Executa o pipeline RAG:
    1. Recupera contexto do Supabase
    2. Gera resposta do modelo da OpenAI com base nesse contexto
    """
    context = retrieve_relevant_data(query)
    llm = get_openai_agent()

    full_prompt = f"{SYSTEM_PROMPT}\n\nDados:\n{context}\n\nPergunta do usuário: {query}"
    response = llm.invoke(full_prompt)

    return response
