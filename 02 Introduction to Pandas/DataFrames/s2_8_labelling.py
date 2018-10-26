import pandas as pd

course = ['Python','Ruby','Excel','C++']

day = ['Mon', 'Tue', 'Tue', 'Wed']

price = [5,10,15,20]

sale = [2,3,5,7]

column_labels = ['Course', 'Day', 'Price', 'Sale']

column_names = [course,day,price,sale]

master_list = list(zip(column_labels,column_names))

# print(master_list)

sales_data = dict(master_list)

df_sales = pd.DataFrame(sales_data)

print(df_sales)

column_labels = ['Course', 'Day', 'Price', '24HR Sale Price']

df_sales.columns = column_labels
print(df_sales)
