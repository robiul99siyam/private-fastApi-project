from pydantic  import  BaseModel
from typing import List

class BlogBaseModel(BaseModel):
    title : str
    body  : str
    user_id : int

class Blog(BaseModel):
    title : str
    body : str
    class Config():
        from_attributes = True   

class UserBaseModel(BaseModel):
    name : str
    email : str
    password : str


class ShowUserBaseModel(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = []
    class Config():
        from_attributes = True


class showBlogModel(BaseModel):
    title : str
    body : str
    creator : ShowUserBaseModel
    class Config():
        from_attributes = True


class Login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None