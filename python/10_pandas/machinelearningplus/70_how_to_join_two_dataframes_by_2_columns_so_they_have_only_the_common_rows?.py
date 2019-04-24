"""
Problem Statement : 70. How to join two dataframes by 2 columns so they have only the common rows?
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
print("\nDataFrame 'df2':")
print(df2)

# Joining dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’
print("\nJoining dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’:")
print(pd.merge(df1, df2, how = 'inner', left_on = ['fruits', 'weight'], right_on = ['pazham', 'kilo'], suffixes = ['_left', '_right']))
