import numpy as np
import pandas as pd

new_array = np.arange(0,10).reshape(2,5)
# print(new_array)

# Convert to a DataFrame
# df = pd.DataFrame(data=new_array)
# print(df)

# Add column names
df = pd.DataFrame(data=new_array, columns=['A','B','C','D','E'])
print(df)
