import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
stock_prices = pd.read_csv('../sample_data/03 Data Analysis/intel_stock_price.csv')

# print(stock_prices)

stock_prices.plot(y='price', kind='bar')

plt.xlabel('month')

plt.show()
