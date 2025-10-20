"""
Serviço para interpretar texto livre e converter em uma transação.
"""
from app.agent.langchain_agent import get_openai_agent
from app.schemas.transaction_schema import TransactionCreate
from datetime import datetime
import re

class TransactionParserService:
    @staticmethod
    def parse_text_to_transaction(text: str) -> TransactionCreate:
        """
        Usa IA da OpenAI para entender um texto livre e extrair:
        tipo, descrição, valor e data.
        """
        llm = get_openai_agent()
        
        prompt = f"""
        Extraia as informações abaixo do texto, retornando em formato JSON:
        - type: "income" ou "expense"
        - description: descrição breve do gasto ou receita
        - amount: valor numérico em reais
        - date: data no formato ISO (YYYY-MM-DD)
        
        Texto: "{text}"
        """

        result = llm.invoke(prompt)
        text_result = str(result.content) if hasattr(result, "content") else str(result)
        
        # Se a resposta contiver um JSON válido, tentamos parsear
        import json
        try:
            data = json.loads(text_result)
        except json.JSONDecodeError:
            # fallback simples por regex se IA não retornar JSON
            amount_match = re.search(r"(\d+([.,]\d{1,2})?)", text)
            amount = float(amount_match.group(1).replace(",", ".")) if amount_match else 0
            type_ = "expense" if any(x in text.lower() for x in ["gastei", "paguei", "comprei"]) else "income"
            description = text
            date = datetime.now().date().isoformat()
            data = {
                "type": type_,
                "description": description,
                "amount": amount,
                "date": date
            }

        return TransactionCreate(**data)
