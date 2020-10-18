#input will be an array of the form [0 1 0 1 1 0 1 0 0 1 0 ... 0 1 0 1 1 0 0 1]
import EmoteModel
import time

def weigh(prediction):
    happyRatio = prediction.count(0) / prediction.count(1)
    return happyRatio

def clock():
    logreg, count_vectors = EmoteModel.init_model()
    ratioDict = {}
    while True:
        tweets = ["ello", "mememan", "gnight"] #grab 10 tweets from the last 10 seconds
        prediction = EmoteModel.make_prediction(logreg, count_vectors, tweets)
        #update_color(weigh(prediction))
        ratioDict[time.time()] = weigh(prediction)
        time.sleep(10)

def findAnomalies(baseline, ratioDict):
    ratios = ratioDict.values()
    baseline = sum(ratios) / len(ratios)
    distances = lambda x: abs(ratios[x] - baseline)
    maxValue = max(distances)
    return list(ratioDict.keys())[list(ratioDict.values()).index(maxValue)]
