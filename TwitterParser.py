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

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

def fetchTweets(language, date_lim, numTweets):
    # query encoded to acceptable URL query
    # query = "+".join([urllib.parse.quote(s) for s in query.split()])
    query = 'the OR i OR to OR a OR and OR is OR in OR it OR you OR of OR tinyurl.com OR for OR on OR my OR ‘s OR that OR at OR with OR me OR do OR have OR just OR this OR be OR n’t OR so OR are OR ‘m OR not OR was OR but OR out OR up OR what OR now OR new OR from OR your OR like OR good OR no OR get OR all OR about OR we OR if OR time OR as OR day OR will OR one OR twitter OR how OR can OR some OR an OR am OR by OR going OR they OR go OR or OR has OR rt OR know OR today OR there OR love OR more OR work OR  OR too OR got OR he OR 2 OR back OR think OR did OR lol OR when OR see OR really OR had OR great OR off OR would OR need OR here OR thanks OR been OR blog OR still OR people OR who OR night OR ‘ll OR want OR why OR bit.ly OR home OR '

    # fetches an iterable collection of the
    # - specified number of tweets (numTweets)
    # - starting from the date specified, (date_lim)
    # - in whatever language, (language)
    # - in the search query (query)
    tweets = tw.Cursor(api.search, q = query, lang = language, since = date_lim).items(numTweets)

    # stores the text of all the processed tweets as a string array
    # strings starting with @RT are retweets
    data = [TweetProcessor.process(tweet.text) for tweet in tweets]

    return data
