from fastapi import FastAPI,Depends,status,HTTPException
from schemas import BlogBaseModel,UserBaseModel,ShowUserBaseModel,showBlogModel
import models
from database import engine,get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import List
from routers import blog,user,login
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.routers)
app.include_router(user.routers)
app.include_router(login.routers)



