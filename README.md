# 💰 FinAI — Assistente Financeiro com IA

Projeto desenvolvido em **FastAPI + LangChain + OpenAI + Supabase**, que permite:
- Registrar transações por texto natural (ex: “gastei 80 reais com gasolina hoje”)
- Consultar relatórios e tendências financeiras
- Interagir com um agente de IA contextual

## ⚙️ Tecnologias
- Python 3.11+
- FastAPI
- Supabase (PostgreSQL)
- LangChain + OpenAI
- Pydantic

## 🚀 Execução
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Acesse a documentação da API em:
👉 http://127.0.0.1:8000/docs