import numpy as np
import pandas as pd

print(pd.__version__)
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(data=arr, index=labels))
print(pd.Series(data=d))
print(pd.Series(data=[sum,print,len]))
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)
print(ser1['USA'])
print(ser1+ser2)
