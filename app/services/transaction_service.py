from app.core.supabase_client import get_supabase_client
from app.schemas.transaction_schema import TransactionCreate
from datetime import datetime

class TransactionService:
    table_name = "transactions"

    @staticmethod
    def create_transaction(data: TransactionCreate):
        """
        Insere uma nova transação no banco de dados.
        """
        supabase = get_supabase_client()
        record = data.model_dump()

        # converte datetime em string antes de enviar
        if isinstance(record.get("date"), datetime):
            record["date"] = record["date"].isoformat()

        response = supabase.table(TransactionService.table_name).insert(record).execute()

        if response.data:
            return {"message": "Transação criada com sucesso!", "data": response.data[0]}
        else:
            return {"error": "Erro ao criar transação", "details": response}

    @staticmethod
    def list_transactions():
        """
        Retorna todas as transações do banco.
        """
        supabase = get_supabase_client()
        response = supabase.table(TransactionService.table_name).select("*").execute()
        return response.data or []

    @staticmethod
    def get_transaction_by_id(transaction_id: str):
        """
        Busca uma transação específica.
        """
        supabase = get_supabase_client()
        response = supabase.table(TransactionService.table_name).select("*").eq("id", transaction_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete_transaction(transaction_id: str):
        """
        Remove uma transação pelo ID.
        """
        supabase = get_supabase_client()
        response = supabase.table(TransactionService.table_name).delete().eq("id", transaction_id).execute()
        return {"message": "Transação deletada com sucesso!"}
