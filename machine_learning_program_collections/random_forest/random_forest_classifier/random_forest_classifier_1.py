import os
from sklearn import datasets
import sklearn.datasets
import sklearn.ensemble
import numpy as np


iris = sklearn.datasets.load_iris()
# Check how did we categorize the iris.data and iris.target, check with chatgpt with examples
train, test, labels_train, labels_test  = sklearn.model_selection.train_test_split(iris.data, iris.target, train_size=0.80)

rf = sklearn.ensemble.RandomForestClassifier(n_estimators = 500)
rf.fit(train, labels_train)


result = rf.score(test, labels_test)       
print(result)

