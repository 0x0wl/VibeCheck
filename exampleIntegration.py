#input will be an array of the form [0 1 0 1 1 0 1 0 0 1 0 ... 0 1 0 1 1 0 0 1]
import EmoteModel
import time
import TwitterParser

def weigh(prediction):
    listpred = prediction.tolist()
    #print(listpred)
    #print(listpred.count(0), listpred.count(1))
    happyRatio = listpred.count(0) / len(listpred)
    return happyRatio

def clock():
    logreg, count_vectors = EmoteModel.init_model()
    ratioDict = {}
    while True:
        tweets = TwitterParser.fetchTweets(language='en', numTweets=10) #grab 10 tweets from the last 10 seconds
        print(tweets[0])
        prediction = EmoteModel.make_prediction(logreg, count_vectors, tweets)
        #update_color(weigh(prediction))
        #ratioDict[time.time()] = weigh(prediction)
        print(str(int(weigh(prediction)*100)) + "% happy")
        time.sleep(15)

def cycle(logreg, count_vectors):
    tweets = TwitterParser.fetchTweets(language='en', numTweets=10) #grab 10 tweets from the last 10 seconds
    #print(tweets[0])
    prediction = EmoteModel.make_prediction(logreg, count_vectors, tweets)
    #update_color(weigh(prediction))
    #ratioDict[time.time()] = weigh(prediction)
    return int(weigh(prediction)*100)

       
def findAnomalies(baseline, ratioDict):
    ratios = ratioDict.values()
    baseline = sum(ratios) / len(ratios)
    distances = lambda x: abs(ratios[x] - baseline)
    maxValue = max(distances)
    return list(ratioDict.keys())[list(ratioDict.values()).index(maxValue)]


