from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TransactionCreate(BaseModel):
    type: str = Field(..., description="Tipo da transação: 'income' ou 'expense'")
    description: str
    amount: float
    date: datetime

class TransactionResponse(TransactionCreate):
    id: str
    user_id: Optional[str] = None
