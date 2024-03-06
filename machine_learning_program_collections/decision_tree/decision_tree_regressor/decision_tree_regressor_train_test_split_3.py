import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# Split the data in test and train
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Training data
# train_X:    Training dataset
# train_y:    Traget variable for training, corresponding to train_X dataset

# Validation or test Data
# val_X:      Validation dataset, will be used to evaluate the performance of your machine learning model during training
# val_y:      target variable to validate the model

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print(val_predictions[:10])
# print the top few actual prices from validation data
print(val_y)

# Calculate the Mean absolute error
val_mae = mean_absolute_error(val_y, val_predictions)
# uncomment following line to see the validation_mae
print(val_mae)

