import os


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'GREGOR BZISHROVSKII'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/jirnich'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True