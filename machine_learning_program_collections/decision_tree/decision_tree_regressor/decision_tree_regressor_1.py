# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


# Path of the file to read
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)

y = home_data['SalePrice']

# Create the list of features below
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

iowa_model = DecisionTreeRegressor(random_state=1)
# Fit the model
iowa_model.fit(X,y)

predictions = iowa_model.predict(X)
# print(predictions)

######### End of the code foe decision TRee Regressor ################



######### Test the code with some other dataset or we can do test/train split ####
# Select data corresponding to features in feature_names
home_data1 = pd.read_csv("test.csv")
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
X1 = home_data1[feature_names]
# iowa_model.fit(X1,y)
predictions = iowa_model.predict(X1.head(100))
print(predictions)