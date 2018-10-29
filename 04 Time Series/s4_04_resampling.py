import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/resampling_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

weekly_mean = sales_data.resample('M').sum()


print(weekly_mean)
