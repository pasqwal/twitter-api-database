# pylint: disable=missing-docstring

from flask import Flask
from flask_restx import Api

from .db import tweet_repository
from .models import Tweet
tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))

def create_app():
    app = Flask(__name__)

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False

    return app
