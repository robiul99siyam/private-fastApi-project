from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from schemas import showBlogModel,BlogBaseModel,UserBaseModel
from sqlalchemy.orm import Session
from database import get_db
from respository.blogs import get_all,create_blog,update_blogs,delete_blogs,get_blog_from_db
from oauth2 import get_current_user


routers = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@routers.get("/" , response_model=List[showBlogModel])

async def All(db:Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return get_all(db)


@routers.post("/",)
async def create(blog : BlogBaseModel , db: Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return create_blog(blog,db)
  

@routers.get("/{id}")
async def get_blog_route(id: int, db: Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):  # Renamed the route handler
    return get_blog_from_db(id, db) 



@routers.put('/{id}',status_code=status.HTTP_202_ACCEPTED)

def update(id:int,blog:BlogBaseModel,db: Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return update_blogs(id,blog,db)



@routers.delete("/{id}",status_code=status.HTTP_202_ACCEPTED)

def delete(id:int,db: Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
   return delete_blogs(id,db)