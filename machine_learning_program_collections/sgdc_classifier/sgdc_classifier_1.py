import os
from sklearn import datasets
import sklearn.datasets
import sklearn.ensemble
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import linear_model


iris = sklearn.datasets.load_iris()
# print(iris.data)

X = iris.data
Y = iris.target


minmax_scaler = MinMaxScaler(feature_range=(0,1))
minmax_scaler.fit(X)
X = minmax_scaler.transform(X)
# print(X)

# Check how did we categorize the iris.data and iris.target, check with chatgpt with examples
train, test, labels_train, labels_test  = sklearn.model_selection.train_test_split(iris.data, iris.target, train_size=0.90)

# print(test)
# print(train)
# print(iris.target)
# print(iris.data)
# print(labels_test)
# print(labels_train)
# print(labels_train.shape)
# print(labels_test.shape)


D = np.c_[train, labels_train]
# print(D)

np.savetxt('iris_train.csv', D, delimiter=",")

chunksize = 25
for chunk in pd.read_csv('iris_train.csv', header=None, chunksize=chunksize):
    train_sub = chunk
    Y = train_sub[4]
    X = train_sub.drop([4], axis=1)
    clf = linear_model.SGDClassifier()
    clf.partial_fit(X,Y, classes = np.unique(Y))
    print(clf.coef_)
    # clf.predict(test)
    pred = clf.predict(test)
    print(pred)
    print(accuracy_score(pred, labels_test))


