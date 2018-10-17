import pandas as pd
import matplotlib.pyplot as plt


# Import our data file
stock_prices = pd.read_csv('../sample_data/03 Data Analysis/intel_stock_price.csv')

# print(stock_prices['price'].max())

print(stock_prices['price'].mean())

# Construct the mean percentage per year: mean
mean = stock_prices.mean(axis='columns')

# Plot the average percentage per year
mean.plot()
plt.show()
