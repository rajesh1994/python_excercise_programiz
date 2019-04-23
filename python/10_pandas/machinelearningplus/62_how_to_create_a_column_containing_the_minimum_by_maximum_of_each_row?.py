"""
Problem Statement : 62. How to create a column containing the minimum by maximum of each row?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
print("DataFrame 'df':")
print(df)

# Solution 1 : Minimum by maximum of each row
min_by_max1 = df.apply(lambda x : np.min(x) / np.max(x), axis = 1)
print("\nSolution 1 : Minimum by maximum of each row")
print(round(min_by_max1, 2))

# Solution 2 : Minimum by maximum of each row
min_by_max2 = np.min(df, axis = 1) / np.max(df, axis = 1)
print("\nSolution 2 : Minimum by maximum of each row")
print(round(min_by_max2, 2))
