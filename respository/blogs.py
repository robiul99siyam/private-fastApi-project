from sqlalchemy.orm import Session
from models import Blogs
from fastapi import HTTPException,status

def get_all(db:Session):
    blogs = db.query(Blogs).all()
    return blogs

def create_blog(blog, db:Session):
    new_blogs = Blogs(
        title = blog.title,
        body = blog.body,
        user_id = blog.user_id
    )

    db.add(new_blogs)
    db.commit()
    db.refresh(new_blogs)
    return new_blogs



def get_blog_from_db(id: int, db: Session):  # Renamed the database function
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User not available {id}')
    return blog



def update_blogs(id:int,blog,db:Session):
    blogs= db.query(Blogs).filter(Blogs.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog not avaliable {id}')
    blogs.update(blog.dict())
    db.commit()
    return "Update Done"


def delete_blogs(id:int,db:Session):
    blogs = db.query(Blogs).filter(Blogs.id == id).first()

    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog not avaliable {id}')
    db.delete(blogs)
    db.commit()
    return "delete done"