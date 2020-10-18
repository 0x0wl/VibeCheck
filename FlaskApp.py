from flask import Flask
import TweetParser
app = Flask(__Controller__)

@app.route("/start?=<start>/end?=<end>")
def getTweet(start, end):
    TweetParser.fetchTweets("", "en", start, 900)
