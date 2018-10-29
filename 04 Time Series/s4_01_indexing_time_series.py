import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

# print(sales_data)


# morning_sale = sales_data.loc['2010-12-01 08:35:00', 'Description']

# morning_sale = sales_data.loc['2010-12-01 08:26:00']

morning_sales = sales_data.loc['2010-12-01 08:26:00':'2010-12-01 09:00:00']

print(morning_sales)
