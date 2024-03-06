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

# Convert string data to DataFrame
# df = pd.read_csv(StringIO(data), parse_dates=['date'])

# Convert dates to ordinal numbers
df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())

# Fit linear regression model
X = df[['date_ordinal']]
y = df['balance']
model = LinearRegression().fit(X, y)

# Predict balance for future dates until balance is less than or equal to 0
current_date = df['date'].iloc[-1]
while True:
    current_date += timedelta(days=1)
    predicted_balance = model.predict([[current_date.toordinal()]])
    if predicted_balance <= 0:
        break

print(f"Estimated date when balance will be zero: {current_date.strftime('%m/%d/%Y')}")

##############################################################################
