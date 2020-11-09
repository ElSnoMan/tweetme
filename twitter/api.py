import os
import tweepy


class Twitter:
    def __init__(self) -> None:
        self.auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
        self.auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
        self.api = tweepy.API(self.auth)
