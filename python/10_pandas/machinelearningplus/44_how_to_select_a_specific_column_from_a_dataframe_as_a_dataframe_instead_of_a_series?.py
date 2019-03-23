"""
Problem Statement : 44. How to select a specific column from a dataframe as a dataframe instead of a series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df1'
df1 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns = [list('abcde')])

# First column in df1 as a DataFrame
print("First column in df1 as a DataFrame:")
print(type([['a']]))
print(type(df1.loc[:, ['a']]))
print(type(df1.iloc[:, [0]]))

# First column in df1 as a series
print("First column in df1 as a series:")
print(type(df1.a))
print(type(df1['a']))
print(type(df1.loc[:, 'a']))
print(type(df1.iloc[:, 1]))
