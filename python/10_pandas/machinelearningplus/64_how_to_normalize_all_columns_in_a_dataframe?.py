"""
Problem Statement : 64. How to normalize all columns in a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy  as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
print("DataFrame 'df':")
print(df)

# Normalize all columns of df by subtracting the column mean and divide by standard deviation
"""
col_mean = df.apply(lambda x : x.mean().round(2))
print("\nColumn mean:")
print(col_mean)

col_std = df.apply(lambda x : x.std().round(2))
print("\nColumn standard deviation:")
print(col_std)
"""

output1 = df.apply(lambda x : ((x - x.mean()) / x.std()).round(2))
print("\nNormalize all columns of df by subtracting the column mean and divide by standard deviation:")
print(output1)

# Range all columns of df such that the minimum value in each column is 0 and max is 1
output2 = df.apply(lambda x : ((x.max() - x) / (x.max() - x.min())).round(2))
print("\nRange all columns of df such that the minimum value in each column is 0 and max is 1:")
print(output2)
