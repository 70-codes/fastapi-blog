from fastapi import APIRouter, Depends, HTTPException, status
import schemas
from sqlalchemy.orm import Session
from database import get_db
from models import User
from hashing import Hash
from JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from oauth2 import get_current_user


auth_router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@auth_router.post('/')
async def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Invalid Credentials"
                            )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Incorrect password"
                            )
    # genetate jwt token and return it
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}