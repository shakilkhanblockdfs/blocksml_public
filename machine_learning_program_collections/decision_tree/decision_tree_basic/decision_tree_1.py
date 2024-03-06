from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

'''
Data:
Let's assume we have a small dataset of fruits:

weight (grams): Weight of the fruit
texture: 0 for smooth skin and 1 for bumpy skin
label: 0 for apple and 1 for orange
'''

# Features and labels
X = [[150, 0], [170, 0], [140, 1], [130, 1]]  # 0: smooth, 1: bumpy
y = [0, 0, 1, 1]  # 0: apple, 1: orange

# Initialize and train the decision tree
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# Predict a new sample
new_sample = [[160, 0]]
prediction = clf.predict(new_sample)
print(f"Prediction for the new sample: {prediction}")  # Should output [0] for apple

# Visualize the decision tree
fig, ax = plt.subplots(figsize=(12, 12))
tree.plot_tree(clf, filled=True, feature_names=["weight", "texture"], class_names=["apple", "orange"])
plt.show()
