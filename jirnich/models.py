import os
from datetime import datetime, timedelta

from flask import current_app
from flask_login import UserMixin
from jwt import encode
from werkzeug.security import check_password_hash, generate_password_hash

from jirnich.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.id}: {self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(
            password, method='pbkdf2:sha256:1000'
        )

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_token(self):
        return encode(
            {'reset_password': self.username,
             'exp': datetime.utcnow() + timedelta(minutes=30)},
            current_app.config['SECRET_KEY']
        )


class Text(db.Model):
    __tablename__ = 'Text'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Text: {self.id}'
