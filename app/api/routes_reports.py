from fastapi import APIRouter
from app.services.report_service import ReportService

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/summary")
def get_financial_summary():
    """Retorna um resumo financeiro geral."""
    return ReportService.get_summary()
