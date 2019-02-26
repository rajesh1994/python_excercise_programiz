"""
Problem Statement : 2.0 How to select a particluar item in a dataframe
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Method 1 : Using 'iloc[]'
print("\nMethod 1 : Using 'iloc[]':")
print(df.iloc[0][0])

# Method 2 : Using 'loc[]'
print("\nMethod 2 : Using 'loc[]':")
print(df.loc[0]['A'])

# Method 3 : Using 'at[]'
print("\nMethod 3 : Using 'at[]':")
print(df.at[0, 'A'])

# Method 4 : Using 'iat[]'
print("\nMethod 4 : Using 'iat[]':")
print(df.iat[0, 0])
