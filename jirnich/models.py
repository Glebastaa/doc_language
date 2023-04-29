from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
import datetime


DeclBase = declarative_base()


class User(DeclBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    email = Column(String(30), nullable=False, unique=True)
    password_hash = Column(String(100), nullable=False)


class Text(DeclBase):
    __tablename__ = 'Text'
    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __init__(self, text):
        self.text = text


DeclBase.create_all()
