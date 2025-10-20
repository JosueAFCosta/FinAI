from app.core.supabase_client import get_supabase_client

def get_db():
    """
    Retorna uma instância do cliente do Supabase para ser usada nas rotas.
    """
    return get_supabase_client()
