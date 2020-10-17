import os
import tweepy as tw
import pandas as pd

api_key = ""
api_secret = ""
token = ""

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

query = input()
date_lim = input()
tweets = input()
tweets = tw.Cursor(api.search, q = query, lang = "en", since = date_lim).items(tweets)

for tweet in tweets:
    print(tweet.text)
