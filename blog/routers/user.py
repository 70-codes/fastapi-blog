from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
import schemas
from database import get_db
from sqlalchemy.orm import Session
from repository import user_repo
from oauth2 import get_current_user


user_router = APIRouter(
    prefix='/user',
    tags=["User"]
)

@user_router.post('/')
async def create_user(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> schemas.UserResponse:
    return user_repo.create


@user_router.get('/')
async def get_all_users(db: Session = Depends(get_db)) -> List[schemas.UserResponse]:
    
    return user_repo.get_all(db)
    
@user_router.get('/{id}')
async def get_user_by_id(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)) ->schemas.UserResponse:
    return user_repo(id, db)