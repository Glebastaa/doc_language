import os
from flask import Flask
from .database import db
from .main.views import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
