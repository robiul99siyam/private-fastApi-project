from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends,status,HTTPException,APIRouter
from database import get_db
from models import User
from schemas import ShowUserBaseModel,UserBaseModel
from typing import List
from hashing import Hash
from oauth2 import get_current_user



routers = APIRouter(
    prefix="/users",
    tags=['Users']
)

@routers.post("/",response_model=ShowUserBaseModel)

async def create_user(request:UserBaseModel,db: Session = Depends(get_db)):

    hashedPasword = Hash.bcrypt(request.password)
    new_users = User(name = request.name , email = request.email , password = hashedPasword)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users


@routers.get("/{id}",response_model=ShowUserBaseModel)

async def user_get(id:int, db: Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    users = db.query(User).filter(User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'users not avaliable {id}')
    return users

@routers.get("/",status_code=status.HTTP_200_OK,response_model=List[ShowUserBaseModel])

async def user_read(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users 