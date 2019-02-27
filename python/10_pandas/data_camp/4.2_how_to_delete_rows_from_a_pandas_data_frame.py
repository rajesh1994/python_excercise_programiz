"""
Problem Statement : 4.2 Deleting a Row from a DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df':
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [87, 67, 56]]), index = [1, 2, 3, 4, 5], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Deleting a row from a DataFrame
# Drop the row at index 3
df.drop(3, axis = 0, inplace = True)
print("\nDrop the row at index 3:")
print(df)
# Drop the row at index 1
df.drop(1, axis = 0, inplace = True)
print("\nDrop the row at index 1:")
print(df)
