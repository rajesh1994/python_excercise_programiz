"""
Problem Statement : 51. How to get the row number of the nth largest value in a column?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10, -1), columns = list('abc'))
print("DataFrame df is:")
print(df)

# Find the row position of the 5th largest value of column 'a' in df.
n = 5
print("Row position of the 4th largest value of column 'a' in df")
print(df['a'].argsort()[::-1][n])
