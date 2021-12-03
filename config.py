# config.py
# pylint: disable=missing-docstring

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


def get_config():
    environnement = environ.get('FLASK_ENV')
    Config = ProductionConfig
    if environnement == 'production':
        return ProductionConfig
    elif environnement == 'development':
        return DevelopmentConfig
    return TestingConfig

class Config():
    SWAGGER_UI_DOC_EXPANSION = 'list'
    SWAGGER_UI_REQUEST_DURATION = True

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # The replace() call is to ensure that the URI starts with 'postgresql://' and not just 'postgres://' as it used to be (this is a back-compability hack)
    #SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1)
    #SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
