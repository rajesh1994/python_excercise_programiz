"""
Problem Statement : 7.0 How To Create an Empty DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Method 1
# Initialize empty DataFrame 'df'
df = pd.DataFrame(data = np.nan, index = [0, 1, 2, 3, 4], columns = ['A', 'B', 'C'])
print("Method 1:\nEmpty DataFrame 'df':")
print(df)

# Method 2
# Initialize empty DataFrame 'df'
df = pd.DataFrame(index = [1, 2, 3, 4, 5], columns = ['A', 'B'], dtype = 'float')
print("\nMethod 2:\nEmpty DataFrame 'df':")
print(df)
