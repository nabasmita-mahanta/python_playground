import pandas as pd

print(pd.read_csv('example.csv'))
df = pd.read_csv('example.csv')
print(df)
print(df.to_csv('My_output',index= False))
print(pd.read_csv('My_output'))
print(pd.read_excel('Excel_Sample.xlsx',sheet_name= 'Sheet1'))
print(pd.read_excel('C:\\Users\Abhinov\Downloads\Annexure-1 GP level training 2023-24.xlsx',sheet_name= 'Table 1'))
