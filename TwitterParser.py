import os
import tweepy as tw
import pandas as pd
import urllib.parse
from nltk.corpus import stopwords
import nltk.stem
import string

api_key = ""
api_secret = ""
token = ""

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def fetchTweets(query, language, date_lim, numTweets):
    # query encoded to acceptable URL query
    query = "+".join([urllib.parse.quote(s) for s in query.split()])

    # fetches an iterable collection of the
    # - specified number of tweets (numTweets)
    # - starting from the date specified, (date_lim)
    # - in whatever language, (language)
    # - in the search query (query)
    tweets = tw.Cursor(api.search, q = query, lang = language, since = date_lim).items(numTweets)

    # stores the text of all the processed tweets as a string array
    # strings starting with @RT are retweets
    data = [TweeterProcessor.process(tweet.text) for tweet in tweets]

    return tweets
