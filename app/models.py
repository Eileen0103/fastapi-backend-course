from sqlalchemy import Column,Date,Integer,String,Boolean
from .database import Base

#Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)
    priority = Column(Integer, default=1)


class User(Base):
    __tablename__="Users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True) 
    password = Column(String, nullable=False)               
    email = Column(String, nullable=False, unique=True)     
    status = Column(String, default="active", nullable=False)  
