import pandas as pd

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv')

# Print df to make sure it works
# print(df)

# How to check data type
# print(type(df))

# How to check df shape
# print(df.shape)

# View column names
# print(df.columns)

# Inspect first tows of data
# print(df.head(10))

# Inspect last rows of data
# print(df.tail(2))

# View summary df info
# print(df.info())

# View open column
# pen = df['Open']
# print(open)

#print(open.head())

# View one or more columns side by side
# print(df[['Open', 'Close']].head())

# Using the describe method
# print(df.describe())
