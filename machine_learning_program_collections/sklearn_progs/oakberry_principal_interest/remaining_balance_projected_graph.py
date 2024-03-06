import numpy as np
import pandas as pd
import numpy as np

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image           # For using the box plot
import time
from io import StringIO
import pandas as pd
from io import StringIO
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta


df = pd.read_csv("mortgage_principal_interest_balance.csv", parse_dates=['date'])
df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())

# Fit linear regression model
X = df[['date_ordinal']]
y = df['balance']
model = LinearRegression().fit(X, y)

# Predict balance for a range of future dates
date_range = pd.date_range(df['date'].iloc[0], df['date'].iloc[-1] + timedelta(days=365*20))  # Extend by 20 years. Balance would be zero by 2038
predicted_balances = model.predict(date_range.to_frame().applymap(lambda x: x.toordinal()))

# Plot actual data and predictions
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['balance'], label='Actual Balance', marker='o')
plt.plot(date_range, predicted_balances, label='Predicted Balance', linestyle='--')

plt.axhline(0, color='red', linestyle='--')  # Zero line
plt.xlabel('Date')
plt.ylabel('Balance')
plt.title('Actual vs Predicted Balance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
