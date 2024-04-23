import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['Z'])
print(type(df['Z']))
print(df[['W','Z']])
df['new'] = df['W'] + df['Z']
print(df)
df.drop('new', axis=1, inplace= True)
print(df)
print(df.shape)
# selecting columns
print(df[['Z','X']])
# 2 ways of selecting rows
print(df.loc['A']) # label based index location
print(df.iloc[2]) # integer based index location
# selecting subset of rows and columns
print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])
