"""
Rotas relacionadas a transações financeiras.
Inclui CRUD completo e rota para interpretar texto livre via IA.
"""

from fastapi import APIRouter, Body
from app.schemas.transaction_schema import TransactionCreate
from app.services.transaction_service import TransactionService
from app.services.transaction_parser_service import TransactionParserService

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# ==============================================
# 🧾 CRUD tradicional
# ==============================================

@router.post("/")
def create_transaction(data: TransactionCreate):
    """Cria uma nova transação."""
    return TransactionService.create_transaction(data)


@router.get("/")
def list_transactions():
    """Lista todas as transações."""
    return TransactionService.list_transactions()


@router.get("/{transaction_id}")
def get_transaction(transaction_id: str):
    """Obtém uma transação pelo ID."""
    return TransactionService.get_transaction_by_id(transaction_id)


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: str):
    """Deleta uma transação pelo ID."""
    return TransactionService.delete_transaction(transaction_id)


# ==============================================
# 💬 Rota de texto livre (com IA)
# ==============================================

@router.post("/parse")
def parse_and_create_transaction(text: str = Body(..., embed=True)):
    """
    Recebe texto livre (ex: 'gastei 45 reais com uber ontem'),
    interpreta automaticamente com IA e registra no banco.
    """
    # Passo 1: interpreta o texto e converte em TransactionCreate
    transaction_data = TransactionParserService.parse_text_to_transaction(text)

    # Passo 2: cria a transação no banco via serviço existente
    result = TransactionService.create_transaction(transaction_data)

    # Retorna o que foi interpretado e o resultado do banco
    return {
        "parsed_data": transaction_data,
        "result": result
    }
