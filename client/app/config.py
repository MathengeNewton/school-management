import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    #debug mode for development
    DEBUG = os.getenv('DEBUG', 'True')
    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    # App Config - the minimal footprint
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')
    # Database - the minimal footprint    
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

