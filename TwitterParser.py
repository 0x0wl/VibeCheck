import os
import tweepy as tw
import pandas as pd
import TweetProcessor

authFile = open("secret.txt", "r")
key = authFile.readLine()
secret = authFile.readLine()
access_token = authFile.readLine()
access_token_secret = authFile.readLine()

auth = tw.OAuthHandler(key, secret)
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
    data = [TweetProcessor.process(tweet.text) for tweet in tweets]

    return tweets
