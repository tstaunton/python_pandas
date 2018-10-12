import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
stock_prices = pd.read_csv('../sample_data/03 Data Analysis/intel_stock_price.csv')

# print(stock_prices.info())

# Create y-columns
y_columns = ['intel', 'amd']

stock_prices.plot(x='month', y=y_columns)

# Create plot title
plt.title('Monthly stock prices')

# Create a title for y axis
plt.ylabel('Price ($US)')

plt.show()
