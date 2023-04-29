import os

from flask import Flask
from main.views import main


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@127.0.0.1:5432/py_jirnich'
    app.register_blueprint(main)

    return app
