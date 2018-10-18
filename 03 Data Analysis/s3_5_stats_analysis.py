import pandas as pd
import matplotlib.pyplot as plt


# Import our data file
stock_prices = pd.read_csv('../sample_data/03 Data Analysis/tesla.csv')

# print(stock_prices)

# print(stock_prices['Open'].min())

# print(stock_prices['Open'].max())

print(stock_prices['Open'].mean())

# Construct the mean percentage per year: mean
mean = stock_prices.mean(axis='columns')

# Plot the average percentage per year
mean.plot()
plt.show()
