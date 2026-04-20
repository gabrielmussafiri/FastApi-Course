from .database import Base
from sqlalchemy import Column, DateTime , Integer , String , Boolean, func, ForeignKey
from datetime import datetime

class Posts(Base):
    __tablename__='posts'
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean ,default= False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer , ForeignKey("users.id",ondelete="CASCADE"), nullable=False)

class Users(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())