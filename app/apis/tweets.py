from flask_restx import Namespace, Resource, fields


from app.db import tweet_repository
from app.models import Tweet

api = Namespace("tweets")

class MyDateFormat(fields.Raw):
    from datetime import time, datetime
    def format(self, value):
        return time.strftime(value, "%d/%m/%Y %H:%M:%S")


json_tweet = api.model('Tweet', {
    'id': fields.Integer(required=True),
    'text': fields.String(required = True, min_length=1),
    'created_at': fields.DateTime(required=True),
    'updated_at': fields.DateTime,
    })

json_new_tweet = api.model('New tweet', {
    'text': fields.String(required=True, min_length=1),  # Don't allow empty string
})




@api.route('')
@api.response(422, 'Invalid tweet')
class TweetsRessource(Resource):
    # Here we use marshal_list_with (instead of marshal_with) to return a list of tweets
    @api.marshal_list_with(json_tweet)
    def get(self):
        tweets = tweet_repository.all()
        return tweets, 200

    @api.marshal_with(json_tweet, code=201)
    @api.expect(json_new_tweet, validate=True)
    def post(self):
        # No need to verify if 'text' is present in body, or if it is a valid string since we use validate=True
        # body has already been validated using json_new_tweet schema
        text = api.payload['text']
        tweet = Tweet(text)
        tweet_repository.add(tweet)
        return tweet, 201



@api.route("/<int:tweet_id>")
@api.param('tweet_id', 'The tweet unique identifier')
class TweetRessource(Resource):
    @api.response(404, "Tweet not found")   # Used to control JSON response format
    @api.marshal_with(json_tweet)
    def get(self, tweet_id):
        tweet = tweet_repository.get(tweet_id)
        if tweet is None:
            api.abort(404, "Tweet not found")   # abort will throw an exception and break execution flow (equivalent to 'return' keyword for an error)
        else:
            return tweet, 200




    def delete(self, tweet_id):
        tweet = tweet_repository.get(tweet_id)
        if tweet is None:
            api.abort(404)
        tweet_repository.remove(tweet_id)

        return None, 204

    @api.marshal_with(json_tweet, code=200)
    @api.expect(json_new_tweet, validate=True)  # Used to control JSON body format (and validate)
    def patch(self, tweet_id):
        tweet = tweet_repository.get(tweet_id)
        if tweet is None:
            api.abort(404)

        # body is also called payload
        # No need to verify if 'text' is present in body, or if it is a valid string since we use validate=True
        # body has already been validated using json_new_tweet schema
        tweet.text = api.payload['text']
        tweet_repository.update(tweet)
        return tweet, 200





