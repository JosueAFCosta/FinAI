"""
Modelo representando uma transação no banco de dados.
"""
from datetime import datetime
from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    user_id: str
    type: str  # 'expense' ou 'income'
    description: str
    amount: float
    date: datetime
