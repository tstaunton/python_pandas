import pandas as pd

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv')

# Create a conditional to return data over 40.0
# my_open = df['Open'] > 40
# print(my_open)

# Print non-boolean values of variable my_open
# print(df[my_open])

# Perform the above with one line of code
# print(df[df['Open'] < 55.0])
