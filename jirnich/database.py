from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()


def init_db(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    db.session.commit()
