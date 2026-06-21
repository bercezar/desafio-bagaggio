from pydantic import BaseModel, EmailStr
from datetime import datetime

# Http(Json) -> Route -> Pydantic -> Repository -> Entity -> Banco


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
