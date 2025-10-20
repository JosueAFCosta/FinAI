from pydantic import BaseModel

class ReportResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float
