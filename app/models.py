from sqlalchemy import Column,Date,Integer,String,Boolean, column
from .database import Base

#Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__="Users"

    id=Column()
    username=Column()
    password=Column()
    email=Column()