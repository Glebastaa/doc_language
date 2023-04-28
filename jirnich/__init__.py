import os
from flask import Flask
from .database import init_db
from .main.views import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    with app.app_context():
        init_db(app)

    app.register_blueprint(main)

    return app
