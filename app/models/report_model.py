"""
Modelo de relatórios financeiros.
"""
from pydantic import BaseModel

class Report(BaseModel):
    total_income: float
    total_expense: float
    balance: float
