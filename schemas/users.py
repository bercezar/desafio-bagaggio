from pydantic import BaseModel, EmailStr
from datetime import datetime


"""
(HTTP/JSON)
  ↓
Route (FastAPI Controller)
  ↓
Pydantic (Validação de entrada)
  ↓
Repository (Lógica de persistência)
  ↓
ORM Entity (SQLAlchemy Model)
  ↓
Database
"""


class UserCreate(BaseModel):
    name: str
    email: EmailStr  # Verificação do '@'
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    is_activate: bool | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Leitura de objetos do banco
