from sqlalchemy import String,Integer,Column,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blogs(Base):
    __tablename__ = 'blogs'

    id = Column(Integer ,primary_key=True,index=True)
    title = Column(String)
    body  = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")

    def ___repr__(self):
        return f"Blogs Title : {self.title}"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blogs',back_populates='creator')
    def __repr__(self):
        return f"user name {self.name}"