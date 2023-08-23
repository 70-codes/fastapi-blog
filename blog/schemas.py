from pydantic import BaseModel
from typing import List

        
class User(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    
class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        orm_mode = True
    
class UserResponse(BaseModel):
    fname: str
    lname: str
    email: str
    blogs: List[Blog] = []
    
    class Config:
        orm_mode = True
        
        

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: UserResponse

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None