"""
Problem Statement : 45. How to change the order of columns of a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df1'
df1 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns = list('abcde'))
print("df1 is:")
print(df1)

# 1. In df, interchange columns 'a' and 'c'.
print("\nIn df, interchange columns 'a' and 'c':")
print(df1[list('cbade')])

# 2. Create a generic function to interchange two columns, without hardcoding column names.
def switch_columns(df1, col1 = None, col2 = None):
	colnames = df1.columns.tolist()
	i1, i2 = colnames.index(col1), colnames.index(col2)
	colnames[i2], colnames[i1] = colnames[i1], colnames[i2]
	return df1[colnames]
print("\nCreate a generic function to interchange two columns, without hardcoding column names:")
print(switch_columns(df1, 'a', 'c'))

# Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.
print("\nSort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last:")
print(df1.sort_index(axis = 1, ascending = False, inplace = False))
