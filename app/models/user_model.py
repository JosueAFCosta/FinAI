"""
Modelo de usuário (para futuras expansões, autenticação, etc).
"""
from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    email: str
