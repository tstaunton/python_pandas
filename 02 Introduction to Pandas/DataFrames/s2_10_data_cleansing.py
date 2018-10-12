import pandas as pd

# df = pd.read_csv('../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')

# Create a string filepath
filepath = ('../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')

column_names = ['App','Rating','Reviews', 'Size','# of Installs','Type','Price','Last Updated']

# Create DataFrame
df = pd.read_csv(filepath, header=None, names=column_names, na_values='-1')

df.index = df['App']

new_columns = ['Rating','Reviews', 'Size','# of Installs','Type','Price','Last Updated']

df = df[new_columns]

# print(df.head())

# out_csv = 'Google Play Data'
# df.to_csv(out_csv)

out_xlsx = 'Google Play Data.xlsx'
df.to_excel(out_xlsx)

# Info about our CSV file
# print(df.info())

# View the first 30 rows with .head()
# print(df.head(30))
