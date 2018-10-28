import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv', index_col='Date', parse_dates=True)

# print(df.head())

# close_value = df['Close'].values

# print(type(close_value))

# df['Close'].plot(color='g', style='-', legend=True)

# plt.axis(('2017','2018', 0,60))

df.plot(color='blue')

plt.title('Stock Price')

plt.xlabel('Date Range')

plt.ylabel('Price ($)')

# plt.show()

plt.savefig('df.pdf')
