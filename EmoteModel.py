from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
import numpy
import TweetProcessor


from sklearn.linear_model import LogisticRegression

dataset = pandas.read_csv('set.csv')
dataset = dataset.drop('author', axis=1)

dataset = dataset.drop(dataset[dataset.sentiment == 'anger'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'boredom'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'enthusiasm'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'empty'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'fun'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'relief'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'surprise'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'love'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'hate'].index)
#dataset = dataset.drop(dataset[dataset.sentiment == 'neutral'].index)
dataset = dataset.drop(dataset[dataset.sentiment == 'worry'].index)

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
print("processed dataset for gradient descent")


#lsvm = SGDClassifier(random_state=9, max_iter=30, tol=None)
#lsvm.fit(XtCount, y_train)
logreg = LogisticRegression(C=1, max_iter=10000, tol=0.000001)
logreg.fit(XtCount, y_train)
print(logreg.classes_)
y_pred = logreg.predict(XvCount)
print('accuracy: %s' % accuracy_score(y_pred, y_val))


#user input
tweets = ["@NerdIndian Take that back. I am insulted.", "AAA IM SO ANGRY GRR", "i just wanna dance", "I'm feeling very well today!", "I am sad.", "im so mad", "I am depressed", "I am angry", "this is so cool", "greatest feeling ever", "overjoyed by this right now", "i dont know what to do right now"]
tweet_count = count_vectors.transform(tweets)
next_pred = logreg.predict(tweet_count)
print(next_pred)
