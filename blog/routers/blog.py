from fastapi import APIRouter, Depends, status
import schemas
from sqlalchemy.orm import Session
from typing import List
from repository import blog_repo
from database import get_db
from oauth2 import get_current_user

blog_router = APIRouter(
    prefix='/blog',
    tags=["Blogs"]
)

@blog_router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repo.create(request, db)

@blog_router.get('/')
async def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> List[schemas.ShowBlog]:
    return blog_repo.get_all(db)


@blog_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_blog_by_id(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> schemas.ShowBlog:
    return blog_repo.get_by_id(id, db)



@blog_router.put("/{id}")
async def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repo.update(id, request, db)


@blog_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repo.delete(id, db)
