import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

morning_sales = sales_data['Quantity']['2010-12-01']

high_quantity = morning_sales.resample('H').min()

print(high_quantity)
