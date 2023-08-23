#!/home/creed347/anaconda3/envs/fastAPI/bin/python

from fastapi import FastAPI
import uvicorn
from routers import blog, user, authentication

import models
from database import engine

# initiating the application
app = FastAPI()

# initializing the database engine
models.Base.metadata.create_all(engine)

app.include_router(authentication.auth_router)
app.include_router(user.user_router)
app.include_router(blog.blog_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
