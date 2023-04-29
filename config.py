import os


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'GREGOR BZISHROVSKII'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost:5432/py_jirnich')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Настройки почты для аутентификации.
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
