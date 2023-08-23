from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException, status
from hashing import Hash

def create(request, db: Session):
    new_user = User(fname = request.fname, lname = request.lname, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session):
    users = db.query(User).all()
    return users

def get_by_id(id, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"THe user with the id {id} does not exist")
    return user