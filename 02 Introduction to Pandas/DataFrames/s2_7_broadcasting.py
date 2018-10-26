import pandas as pd

# course_sales = {'course':['Python','Ruby','Excel','C++'],
#                'day':['Mon','Tue','Wed','Tue'],
#                'price':[5,10,15,20],
#                'sale':[2,3,5,7]
#                }

# df_sales = pd.DataFrame(course_sales)
# print(df_sales)

course = ['Python','Ruby','Excel','C++']

day = ['Mon', 'Tue', 'Tue', 'Wed']

price = [5,10,15,20]

sale = [2,3,5,7]

column_labels = ['Course', 'Day', 'Price', 'Sale']

column_names = [course,day,price,sale]

master_list = list(zip(column_labels,column_names))

print(master_list)

sales_data = dict(master_list)

df_sales = pd.DataFrame(sales_data)

print(df_sales)

df_sales['New Price'] = 2
print(df_sales)
