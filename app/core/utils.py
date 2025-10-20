"""
Funções auxiliares e genéricas usadas em todo o projeto.
"""
def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
