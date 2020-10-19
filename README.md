# VibeCheck
## HelloWorld2020

Live Demo: http://cygnus.dropout.college:5000

Changes the background color of the website to reflect the current mood of Twitter. 
The color is calculated based off of the predictions of a logistic regression model trained using 10,000 pairings of message content and sentiment from tweets.
The background of the website will then change based off of the intensity of Twitter's happiness or sadness (how many tweets were classified as sad vs happy).
Uses natural language toolkit, numpy, flask, and tweepy.

## How to run VibeCheck
1) Put your Twitter API tokens in secret.txt
2) pip install all the libraries (numpy, tweepy, nltk, pandas, flask, sklearn)
3) python3 FlaskApp.py
4) open index1.html
