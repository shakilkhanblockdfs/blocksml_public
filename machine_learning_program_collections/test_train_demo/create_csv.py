import pandas as pd

# Create a dictionary with the data
data = {
    'LotArea': [5000, 5500, 5600, 4000],                                # All the below are features except the Saleprice
    'YearBuilt': [2019, 2019, 2017, 1970],
    '1stFlrSF': [2, 1, 2, 2],
    '2ndFlrSF': [0, 0, 1, 1],
    'FullBath': [2, 2, 2, 2],
    'BedroomAbvGr': [3, 3, 4, 4],
    'TotRmsAbvGrd': [1, 1, 1, 1],
    'SalePrice': [550000, 450000, 590000, 290000]                            # Target
}

# Create a DataFrame
df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
file_path = "data.csv"

# Save the DataFrame as a CSV file
df.to_csv(file_path, index=False)

print(f"CSV file '{file_path}' has been created with the provided data.")
