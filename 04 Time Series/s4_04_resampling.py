import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

weekly_max = sales_data.loc[:, "Quantity"].resample('W').sum()

print(weekly_max)
