# Groupby allows you to group together rows based off of a column and perform
# an aggregate function on them.
import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
print(df)
byComp = df.groupby('Company')
print(byComp)
print(byComp.mean(numeric_only=True))
byComp = df.groupby('Company')['Sales'].sum()
print(byComp)
byComp = df.groupby('Company')
print(byComp.std(numeric_only=True))
print(df.groupby('Company')['Sales'].sum().loc['FB'])
print(df.groupby('Company').count())
print(df.groupby('Company').min())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])