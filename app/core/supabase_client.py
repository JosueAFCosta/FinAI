from supabase import create_client, Client
from app.config import settings

_supabase: Client = None

def get_supabase_client() -> Client:
    """
    Retorna uma instância do cliente Supabase.
    Cria apenas uma instância global (singleton) para reuso.
    """
    global _supabase
    if _supabase is None:
        _supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    return _supabase
