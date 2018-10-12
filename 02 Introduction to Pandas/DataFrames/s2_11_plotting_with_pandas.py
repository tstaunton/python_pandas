import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv', index_col='Date', parse_dates=True)

# print(df.head())

# open_value = df['Open'].values

# print(type(open_value))

# Lets plot
#plt.plot(open_value)

#plt.show()

# df.plot()
# plt.show()

df['Open'].plot(color='g', style='-', legend=True)

plt.axis(('2017','2018', 0,60))

plt.title('Intel Stock Price')
plt.ylabel('Price')

plt.savefig('df.png')

plt.show()
