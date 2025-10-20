from app.core.supabase_client import get_supabase_client

def test_supabase_connection():
    try:
        supabase = get_supabase_client()
        response = supabase.table("transactions").select("*").execute()
        print("✅ Conexão bem-sucedida com o Supabase!")
        print("Dados retornados:", response.data)
    except Exception as e:
        print("❌ Erro ao conectar com o Supabase:")
        print(e)

if __name__ == "__main__":
    test_supabase_connection()
