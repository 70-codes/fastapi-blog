from sqlalchemy.orm import Session
from models import Blog
from fastapi import status, HTTPException



def create(request, db: Session):
    new_blog = Blog(title=request.title, body=request.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def get_by_id(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog


def update(id,request, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail="Blog does not exist")
    
    blog_data = request.model_dump()
    
    for key, value in blog_data.items():
        setattr(blog, key, value)
    
    db.commit()
    db.refresh(blog)
    return blog


def delete(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"