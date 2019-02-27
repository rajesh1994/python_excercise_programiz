"""
Problem Statement : 4.1 How to Delete Columns From a Pandas Data Frame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 57]]), index = [1.2, 2.4, 4.6, 9.3, 5.3], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Deleting a column from DataFrame
# Drop the column with label 'A'
df.drop('A', axis = 1, inplace= True)
print("\nDrop the column with label 'A:")
print(df)

# Drop the column at Position 1
df.drop(df.columns[[1]], axis = 1)
print("\nDrop the column at Position 1:")
print(df)
