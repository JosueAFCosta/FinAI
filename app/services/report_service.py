class ReportService:
    @staticmethod
    def get_summary():
        """Gera um resumo financeiro geral."""
        return {"total_income": 0, "total_expense": 0, "balance": 0}
