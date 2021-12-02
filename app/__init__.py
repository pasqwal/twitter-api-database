# pylint: disable=missing-docstring

from flask import Flask
from flask_restx import Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    from config import get_config
    app.config.from_object(get_config())
    db.init_app(app)

    migrate.init_app(app, db)
    # cmd to migrate:
    # pipenv run flask db init
    # pipenv run flask db migrate -m "Initial migration"
    # pipenv run flask db upgrade

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False

    return app
