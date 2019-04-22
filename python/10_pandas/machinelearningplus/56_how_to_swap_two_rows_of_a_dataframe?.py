"""
Problem Statement : 56. How to swap two rows of a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.arange(25).reshape(5, -1))
print("DataFrame 'df':")
print(df)

# Solution
def swap_rows(df, i1, i2):
	a, b = df.iloc[i1, :].copy(), df.iloc[i2, :].copy()
	df.iloc[i1, :], df.iloc[i2, :] = b, a
	return df
print("\nSwap two rows of a DataFrame:")
print(swap_rows(df, 1, 2))
