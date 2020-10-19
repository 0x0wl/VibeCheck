import os
import tweepy as tw
import pandas as pd
import TweetProcessor
import urllib

authFile = open("secret.txt", "r")
key = authFile.readline()[:-1]
secret = authFile.readline()[:-1]
access_token = authFile.readline()[:-1]
access_token_secret = authFile.readline()[:-1]

auth = tw.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.verify_credentials()


def fetchTweets(language, numTweets):
    # query encoded to acceptable URL query
    # query = "+".join([urllib.parse.quote(s) for s in query.split()])
    #query = '(the OR i OR to OR a OR and OR is OR in OR it OR you OR of OR tinyurl.com OR for OR on OR my OR ‘s OR that OR at OR with OR me OR do OR have OR just OR this OR be OR n’t OR so OR are OR ‘m OR not OR was OR but OR out OR up OR what OR now OR new OR from OR your OR like OR good OR no OR get OR all OR about OR we OR if OR time OR as OR day OR will OR one OR twitter OR how OR can OR some OR an OR am OR by OR going OR they OR go OR or OR has OR rt OR know OR today OR there OR love OR more OR work OR too OR got OR he OR 2 OR back OR think OR did OR lol OR when OR see OR really OR had OR great OR off OR would OR need OR here OR thanks OR been OR blog OR still OR people OR who OR night OR ‘ll OR want OR why OR bit.ly OR home)'
    #query = 'the'
    #query = "+".join([urllib.parse.quote(s) for s in query.split()])



    #query = "https://api.twitter.com/1.1/search/tweets.json?q=(i%20OR%20to%20OR%20a%20OR%20and%20OR%20is%20OR%20in%20OR%20it%20OR%20you%20OR%20of%20OR%20tinyurl.com%20OR%20for%20OR%20on%20OR%20my%20OR%20%E2%80%98s%20OR%20that%20OR%20at%20OR%20with%20OR%20me%20OR%20do%20OR%20have%20OR%20just%20OR%20this%20OR%20be%20OR%20n%E2%80%99t%20OR%20so)&src=typed_query"
    query = '(i OR to OR a OR and OR is OR in OR it OR you OR of OR tinyurl.com OR for OR on OR my OR ‘s OR that OR at OR with OR me OR do OR have OR just OR this OR be OR n’t OR so)'
    # fetches an iterable collection of the
    # - specified number of tweets (numTweets)
    # - starting from the date specified, (date_lim)
    # - in whatever language, (language)
    # - in the search query (query)
    #tweets = tw.Cursor(api.search, q = query, lang = language).items(numTweets)
    data = []
    for tweet in api.search(q=query, lang="en", rpp=10):
        data.append(TweetProcessor.process(tweet.text))

    #print(tweet.text for tweet in tweets)

    # stores the text of all the processed tweets as a string array
    # strings starting with @RT are retweets
    #data = [TweetProcessor.process(tweet.text) for tweet in tweets]

    return data
