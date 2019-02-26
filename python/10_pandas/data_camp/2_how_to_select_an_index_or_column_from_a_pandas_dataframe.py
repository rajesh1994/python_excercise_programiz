"""
Problem Statement : 2.0 How to select a particluar item
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Method 1 : Using 'iloc[]'
print("Method 1 : Using 'iloc[]':")
print(df.iloc[0][0])

# Method
