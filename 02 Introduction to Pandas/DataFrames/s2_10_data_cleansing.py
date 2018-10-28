import pandas as pd

# df = pd.read_csv('../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')

column_names = ['App', 'Rating', 'Reviews', 'Size', 'Number of Install', 'Type', 'Price', 'Last Updated']

filepath = ('../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')

df = pd.read_csv(filepath, header=None, names=column_names, na_values='-1')

df.index = df['Last Updated']

new_columns = ['App', 'Reviews']

df = df[new_columns]

out_csv = 'Google Play Data'
df.to_csv(out_csv)

out_xlsx = 'Google Play Data EXCEL.xlsx'
df.to_excel(out_xlsx)
