# import pandas as pd
# import numpy as np
# import matplotlib.pylab as plt
# import seaborn as sns
# plt.style.use('ggplot')
# pd.set_option('display.max_columns', 200)
# pd.set_option('display.max_rows', 1000)

# df = pd.read_csv('coaster_db.csv')

# df.drop(['Status'], axis=1)

# # for i in df:
# #     print(df)

# for index, row in df.iterrows():
#     print(index, " ",row)
#     print("-------------------")


# # for i in df:
# #     print(df[i])


###############################

d = {'k':'k11'}
if d.get('k'):
    print(list(d.get('k') + str("2")))
else:
    print(d.get('k1'))