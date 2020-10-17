import os
import urllib.parse
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re

def process(s):
    # converts to lowercase
    s = s.lower()
    # removes punctuation
    s.translate(string.maketrans('', '', string.punctuation))
    # removes stop words
    s = " ".join([word for word in ntlk.tokenize.word_tokenize(s) if not word in stopwords.words("english")])
    # converts words to root words (stemming)
    porter = PorterStemmer()
    s = " ".join([porter.stem(word) for word in ntlk.tokenize.word_tokenize(s)])
    # removes URLs
    s = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", s).split())
    # removes usernames
    s = " ".join(word for word in ntlk.tokenize.word_tokenize(s) if (not word.startsWith("@") and len(word) > 1))
    # removes three-char repitions
    s = re.compile(r"(.)\1{2,}").sub(r"\1\1", s)
