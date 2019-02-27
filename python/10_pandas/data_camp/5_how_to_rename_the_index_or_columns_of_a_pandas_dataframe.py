"""
Problem Statement : 5. How to Rename the Index or Columns of a Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index = [1, 2, 3], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Difining new names of columns 'A', 'B' & 'C'
new_cols = {'A' : 'a', 'B' : 'b', 'C' : 'c'}
# Renaming columns 'A', 'B' & 'C' by using rename() method
df.rename(columns = new_cols, inplace = True)
print("\nRenaming columns 'A', 'B' & 'C' to 'a', 'b' & 'c':")
print(df)

# Difining new names of rows 1, 2 & 3
new_rows = {1 : 'one', 2 : 'two', 3 : 'three'}
# Renaming rows 1, 2, 3 by using rename() method
df.rename(index = new_rows, inplace = True)
print("\nRenaming rows 1, 2 & 3 to 'one', 'two' & 'three':")
print(df)
