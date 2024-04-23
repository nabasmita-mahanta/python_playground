import Data_Frames

booldf = Data_Frames.df > 0
print(booldf)
print(Data_Frames.df[booldf])
print(Data_Frames.df['W'] > 0)
result_df = Data_Frames.df[Data_Frames.df['W'] > 0]
print(result_df)
print(result_df['X'])
print(Data_Frames.df[Data_Frames.df['W'] > 0][['Y','X']])
print(Data_Frames.df[(Data_Frames.df['W']>0) & (Data_Frames.df['Y']>1)])
print(Data_Frames.df[(Data_Frames.df['W']>0) | (Data_Frames.df['Y']>1)])
print(Data_Frames.df.reset_index())
newind = 'CA NY WY OR CO'.split()
print(newind)
Data_Frames.df['States']= newind
print(Data_Frames.df)
print(Data_Frames.df.set_index('States'))
