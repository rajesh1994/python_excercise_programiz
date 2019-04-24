"""
Problem Statement : 67. How to get the particular group of a groupby dataframe by key?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame({'col1' : ['apple', 'banana', 'orange'] * 3, 'col2' : np.random.rand(9), 'cols3' : np.random.randint(0, 15, 9)})
print("DataFrame 'df':")
print(df)

# Solution 1 : Particular group of a groupby dataframe by key
df_grouped = df.groupby(['col1'])
print("\nSolution 1 : Particular group of a groupby dataframe by key:")
print(df_grouped.get_group('apple'))

# Solution 2 : Particular group of a groupby dataframe by key
print("\nSolution 2 : Particular group of a groupby dataframe by key:")
for i, dff in df_grouped:
	if i == 'apple':
		print(dff)
