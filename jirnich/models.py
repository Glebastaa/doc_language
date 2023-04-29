from datetime import datetime

from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from jirnich.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.id}: {self.username}'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Text(db.Model):
    __tablename__ = 'Text'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Text: {self.id}'
