"""
Problem Statement : 71. How to get the positions where values of two columns match?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df1' & 'df2'
df1 = pd.DataFrame({'fruits' : ['apple', 'banana', 'orange'] * 3, 'weight' : ['high', 'medium', 'low'] * 3, 'price' : np.random.randint(0, 15, 9)})
df2 = pd.DataFrame({'pazham' : ['apple', 'banana', 'orange'] * 2, 'kilo' : ['high', 'low'] * 3, 'price' : np.random.randint(0, 15, 6)})
print("DataFrame 'df1':")
print(df1)
print("\nDataFrame 'df':")
print(df2)

# From df1, remove the rows that are present in df2. All three columns must be the same
print("\nFrom df1, remove the rows that are present in df2:")
print(df1[~df1.isin(df2).all(1)])
