import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/small_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

# morning_sale = sales_data.loc['2010-12-01 08:35:00', 'Description']

# time1 = sales_data.loc['2010-12-01 08:26:00']

# time2 = sales_data.loc['2010-12-01']

time3 = sales_data.loc['2010-12-01' : '2010-12-03']

print(time3)
