from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
import numpy
import TweetProcessor

dataset = pandas.read_csv('set.csv')
dataset = dataset.drop('author', axis=1)

dataset['content'] = dataset['content'].apply(TweetProcessor.process)

#debugging
print("loaded dataset...")


label_encoder = preprocessing.LabelEncoder()
y = label_encoder.fit_transform(dataset.sentiment.values)

X_train, X_val, y_train, y_val = train_test_split(dataset.content.values, y, stratify=y, random_state=23, test_size=0.1, shuffle=True) #test_size=0.1?

tf_idf_params = TfidfVectorizer(ngram_range=(1,3))
XtIdf = tf_idf_params.fit_transform(X_train)
XvIdf = tf_idf_params.fit_transform(X_val)

count_vectors = CountVectorizer()
count_vectors.fit(data['content'])
XtCount = count_vect.transform(X_train)
XvCount = count_vect.transform(X_val)

#debugging
print("loaded data for gradient descent...")

lsvm = SGDClassifier(random_state=9, max_iter=15, tol=None)
lsvm.fit(XtCount, y_train)
y_pred = lsvm.predict(XvCount)
print('lsvm using count vectors accuracy %s' % accuracy_score(y_pred, y_val))
