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

# Convert the string data to a DataFrame
df = pd.read_csv("mortgage_principal_interest.csv", parse_dates=['date'])

# Extract year from date
df['year'] = df['date'].dt.year

# Calculate the overall sum and mean for principal and interest columns
principal_sum = df['principal'].sum()
interest_sum = df['interest'].sum()

principal_mean = df['principal'].mean()
interest_mean = df['interest'].mean()

print(f"Total Principal: {principal_sum}")
print(f"Total Interest: {interest_sum}")
print(f"Mean Principal: {principal_mean}")
print(f"Mean Interest: {interest_mean}")

# Calculate the year-wise sum and mean for principal and interest columns
yearwise_sum = df.groupby('year')[['principal', 'interest']].sum()
yearwise_mean = df.groupby('year')[['principal', 'interest']].mean()

print("\nYear-wise Sum:\n", yearwise_sum)
print("\nYear-wise Mean:\n", yearwise_mean)

