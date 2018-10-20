import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/resampling_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

weekly_mean = sales_data.loc[:,'Quantity'].resample('2W').sum()

print(weekly_mean)

# print(weekly_mean.loc['2010-10-31'])

# print(weekly_mean.loc['2010-01-24', 'Quantity'])
