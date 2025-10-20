"""
Responsável por buscar dados no Supabase para o RAG.
"""
from app.core.supabase_client import get_supabase_client
from datetime import datetime, timedelta

def retrieve_relevant_data(query: str):
    """
    Busca e formata dados relevantes das transações com base na pergunta do usuário.
    """
    supabase = get_supabase_client()

    # Recupera todas as transações (você pode filtrar depois)
    response = supabase.table("transactions").select("*").execute()
    transactions = response.data or []

    # Monta um contexto textual simples
    formatted_data = []
    for t in transactions:
        tipo = "receita" if t["type"] == "income" else "despesa"
        linha = f"{t['date'][:10]} - {tipo}: R$ {t['amount']:.2f} ({t['description']})"
        formatted_data.append(linha)

    # Junta tudo num contexto único
    context = "\n".join(formatted_data)

    # Se o banco estiver vazio, devolve contexto genérico
    if not formatted_data:
        context = "Nenhuma transação registrada ainda."

    return context
