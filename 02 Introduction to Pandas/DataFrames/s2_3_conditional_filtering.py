import pandas as pd

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv')

# Conditional Filtering
my_open = df['Open'] > 48.0
print(my_open)

# Show DataFrame where only my_open is True
# print(df[my_open])

# One step option
# print(df[df['Open'] > 55.0])
