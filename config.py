import os


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'
    #Тут нужны настройки для бызы постгреса. Пока на костыле.
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True