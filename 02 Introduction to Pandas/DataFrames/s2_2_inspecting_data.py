import pandas as pd

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv')

# Print the entire DataFrame
# print(df)

# What is the data type?
# print(type(df))

# What is the shape of our DataFrame? (rows, columns)
# print(df.shape)

# Show column names
# print(df.columns)

# Show top rows of DataFrame
# print(df.head())

# Show info summary of DataFrame
# print(df.info())

# Print a column series
# open = df['Open']
# print(open)

# Print columns side by side
# print(df[['Open','Close']].head())

# Using min with DataFrames
# print(df['Open'].min())

# Show mean open value
# print(df['Open'].mean())
