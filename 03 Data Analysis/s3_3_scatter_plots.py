import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
life = pd.read_csv('../sample_data/03 Data Analysis/irish_life_expec.csv')

life.plot(kind='scatter', x='year', y='life expec')

# Add the title
plt.title('Irish Life Expectancy 2000 - 2014')

# Add the x-axis label
plt.xlabel('Age')

# Add the y-axis label
plt.ylabel('Year')

plt.show()
