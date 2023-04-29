import os

from flask import Flask
from flask_migrate import Migrate

from jirnich.database import db
from jirnich.main.views import main
from jirnich.users.views import users


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    migrate = Migrate(app, db)

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
