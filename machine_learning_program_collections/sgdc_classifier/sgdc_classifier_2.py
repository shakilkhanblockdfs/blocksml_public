'''
Import the necessary libraries:

numpy for numerical operations.
SGDClassifier from scikit-learn, which is a linear classifier trained using Stochastic Gradient Descent.
StandardScaler from scikit-learn, which is used for feature scaling.
make_pipeline from scikit-learn, which is used to create a pipeline that automates the data preprocessing and model training steps.
Create sample data:

X is a NumPy array containing four data points, each with two features.
Y is a NumPy array containing the corresponding target labels (1 or 2).
Define a machine learning pipeline:

clf is created using make_pipeline. Inside the pipeline:
StandardScaler() is used to standardize (scale) the input features. Standardization ensures that each feature has a mean of 0 and a standard deviation of 1.
SGDClassifier is the classifier used for training. It's configured to perform a maximum of 1000 iterations and stop when the loss decreases by less than tol=1e-3 (a small tolerance value).
Fit the pipeline to the data:

clf.fit(X, Y) trains the entire pipeline. First, it scales the input data using StandardScaler, and then it fits the SGDClassifier to the scaled data.
Make a prediction:

clf.predict([[-0.8, -1]]) makes a prediction for a new data point [-0.8, -1] using the trained pipeline. The output will be the predicted class label.
In summary, this code demonstrates a simple example of creating a machine learning pipeline in scikit-learn, which includes data preprocessing (scaling) and model training (SGDClassifier). This pipeline can be used to make predictions on new data points efficiently and consistently. In this specific example, it predicts the class label for the data point [-0.8, -1].


'''


import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 0, 2, 2])
# Always scale the input. The most convenient way is to use a pipeline.
clf = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000, tol=1e-3))

clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))
print(clf.predict([[-2,-0.9]]))