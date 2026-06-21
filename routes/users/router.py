from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserResponse, UserUpdate
from repository import users
from database import get_db
from entities.user import User


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    users_email = users.get_user_by_email(db, email=payload.email)
    if users_email:
        raise HTTPException(status_code=400, detail="Email já existente")
    users_newUser = users.create_user(
        db, **payload.model_dump())  # Desempacotamento payload

    return users_newUser


@router.get("/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users_list = users.list_users(db=db, skip=skip, limit=limit)

    return users_list


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não existe")

    found_user = users.get_user(db=db, user_id=user_id)
    return found_user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user_update = users.get_user(db, user_id)
    if not user_update:
        raise HTTPException(status_code=404, detail="Usuário não existe")

    # Conversão somente dos dados enviados
    update_data = payload.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400, detail="Dados ausentes para atualização")

    users_updated = users.update_user(
        db, user=user_update, update_data=update_data)

    return users_updated


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_delete = users.get_user(db, user_id)
    if not user_delete:
        raise HTTPException(status_code=404, detail="Usuário não existe")

    user_deleted = users.delete_user(db=db, user=user_delete)

    return {"message": "Usuário Deletado"}
