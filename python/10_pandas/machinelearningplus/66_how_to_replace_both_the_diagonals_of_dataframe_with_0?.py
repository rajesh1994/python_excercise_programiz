"""
Problem Statement : 66. How to replace both the diagonals of dataframe with 0?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 100).reshape(10, -1))
print("DataFrame 'df':")
print(df)

# Replace both the diagonals of dataframe with 0
for i in range(df.shape[0]):
	df.iat[i, i] = 0
	df.iat[df.shape[0] - i - 1, i] = 0
print("\nReplace both the diagonals of dataframe with 0:")
print(df)
