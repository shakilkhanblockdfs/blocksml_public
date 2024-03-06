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


df = pd.read_csv("mortgage_principal_interest.csv", parse_dates=['date'])

# Calculate the sum and mean for principal and interest columns
principal_sum = df['principal'].sum()
interest_sum = df['interest'].sum()

principal_mean = df['principal'].mean()
interest_mean = df['interest'].mean()

print(f"Total Principal: {principal_sum}")
print(f"Total Interest: {interest_sum}")
print(f"Mean Principal: {principal_mean}")
print(f"Mean Interest: {interest_mean}")






