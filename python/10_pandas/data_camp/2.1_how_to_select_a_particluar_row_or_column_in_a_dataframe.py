"""
Problem Statement : 2.1 How to select a particluar row/column in a dataframe
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Method 1 : Using 'iloc[]' to select row '0'
print("\nMethod 1 : Using 'iloc[]' to select row '0':")
print(df.iloc[0])

# Method 2 : Using 'loc[]' to select column 'A'
print("\nMethod 2 : Using 'loc[]' to select column 'A':")
print(df.loc[:, 'A'])
