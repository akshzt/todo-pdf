from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    done = Column(Boolean, default=False)

