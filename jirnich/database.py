import psycopg2
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, unique=False)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="testdb",
        user="postgres",
        password="mypassword"
    )
    return conn