# 💰 FinAI — Assistente Financeiro com IA

FinAI é um **assistente financeiro inteligente** desenvolvido com **FastAPI, LangChain, OpenAI e Supabase**, capaz de:

- 📥 Registrar transações via texto natural  
  (ex: “gastei 80 reais no mercado ontem”)
- 💬 Responder perguntas sobre suas finanças  
  (ex: “quanto gastei este mês?”)
- 📊 Gerar relatórios e análises automáticas  
- ☁️ Armazenar tudo em banco Supabase de forma segura

---

## 🧠 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| **FastAPI** | Framework backend moderno e performático |
| **LangChain + OpenAI** | Interpretação de linguagem natural (IA) |
| **Supabase (PostgreSQL)** | Banco de dados e autenticação |
| **Pydantic** | Validação e tipagem dos modelos |
| **Uvicorn** | Servidor ASGI rápido para a API |

---

## ⚙️ Estrutura de Pastas

app/
├── agent/ # Lógica da IA (LangChain + OpenAI)
├── api/ # Rotas FastAPI (endpoints)
├── core/ # Configurações e cliente Supabase
├── models/ # Modelos internos (entidades)
├── schemas/ # Schemas Pydantic (validação)
├── services/ # Lógica de negócios
└── main.py # Ponto de entrada da aplicação

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/<SEU_USUARIO>/FinAI.git
cd FinAI

2️⃣ Criar ambiente virtual
    python -m venv venv

3️⃣ Ativar o ambiente
    Windows
    venv\Scripts\activate

    Linux/Mac
    source venv/bin/activate

4️⃣ Instalar dependências
    pip install -r requirements.txt

5️⃣ Configurar variáveis de ambiente
    Crie um arquivo .env na raiz (baseado em .env.example).

6️⃣ Rodar o servidor
    uvicorn app.main:app --reload

7️⃣ Acessar a documentação da API
    👉 http://127.0.0.1:8000/docs

🧩 Exemplo de uso
Registro de transação via IA:


POST /transactions/parse
{
    "text": "gastei 45 reais com uber ontem"
}   

Resposta esperada:
{
    "parsed_data": {
        "type": "expense",
        "description": "uber",
        "amount": 45.0,
        "date": "2025-10-20"},
    "result": {
        "message": "Transação criada com sucesso!",
        "data": { ... }}
}

🔐 Segurança
⚠️ O arquivo .env contém chaves secretas e não deve ser enviado para o GitHub.
Use o arquivo .env.example como referência.

🧑‍💻 Autor
Josué Costa
📍 Desenvolvedor Full Stack | IA e No-Code
💼 GitHub
📧 josue@example.com

⭐ Dica: se curtiu o projeto, dá uma estrela no repositório!
Assim o GitHub recomenda o projeto pra mais devs 🚀