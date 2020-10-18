from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
#from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
import numpy
import TweetProcessor


from sklearn.linear_model import LogisticRegression

def init_model():
    dataset = pandas.read_csv('newset.csv')

    dataset['content'] = dataset['content'].apply(TweetProcessor.process)

    #debugging
    print("loaded dataset...")


    label_encoder = preprocessing.LabelEncoder()
    y = label_encoder.fit_transform(dataset.sentiment.values)

    X_train, X_val, y_train, y_val = train_test_split(dataset.content.values, y, stratify=y, random_state=42, test_size=0.1, shuffle=True) #test_size=0.1?

    count_vectors = CountVectorizer()
    count_vectors.fit(dataset['content'])
    XtCount = count_vectors.transform(X_train)
    XvCount = count_vectors.transform(X_val)

    #debugging
    print("processed dataset for logistic regression")


    #lsvm = SGDClassifier(random_state=9, max_iter=30, tol=None)
    #lsvm.fit(XtCount, y_train)
    logreg = LogisticRegression(C=1, max_iter=1000, tol=0.0001)
    logreg.fit(XtCount, y_train)
    #print(logreg.classes_)
    y_pred = logreg.predict(XvCount)
    print('accuracy: %s' % accuracy_score(y_pred, y_val))

    return logreg, count_vectors

def make_prediction(logreg, count_vectors, tweets = ["@NerdIndian Take that back. I am insulted.", "AAA IM SO ANGRY GRR", "i just wanna dance", "I'm feeling very well today!", "I am sad.", "im so mad", "I am depressed", "I am angry", "this is so cool", "greatest feeling ever", "overjoyed by this right now", "i dont know what to do right now"]
):
    #user input
    tweet_count = count_vectors.transform(tweets)
    next_pred = logreg.predict(tweet_count)
    return next_pred

'''
def main():
    logreg, count_vectors = init_model()
    print(make_prediction(logreg, count_vectors))
'''

#main()
