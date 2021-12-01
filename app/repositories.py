# app/repositories.py
# pylint: disable=missing-docstring

class TweetRepository:
    def __init__(self):
        self.clear()

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1

    def get(self, id):
      for tweet in self.tweets:
          if tweet.id == id:
              return tweet
      return None

    def all(self):
      return self.tweets

    def update(self, tweet):
      tweet.updated()

#    def update(self, tweet):
#      for tweet in self.tweets:
#        if tweet.id == id:
#          tweet.text = value
#          tweet.updated()
#          return tweet
#      return None


    def remove(self, id):
      for tweet in self.tweets:
        if tweet.id == id:
          self.tweets.remove(tweet)

    def clear(self):
      self.tweets = []
      self.next_id = 1
