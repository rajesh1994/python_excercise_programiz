"""
Problem Statement : 3.1 How To Add a Row or Column to a Pandas DataFrame
"""
# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'], index= [2.5, 12.6, 4.8])
print("DataFrame 'df' is:")
print(df)

# Adding a column to a DataFrame
df['D'] = df.index
print("\nAfter adding column 'D' to DataFrame")
print(df)

# Appending a column to a DataFrame
df.loc[:, 'E'] = pd.Series(['5', '6', '1'], index = df.index)
print("\nAfter appending a column 'E' to DataFrame:")
print(df)

# Resetting the index of a DataFrame
df_reset = df.reset_index(level = 0, drop = True)
# Printing resetted index in DataFrame
print("\nResetted index in DataFrame:")
print(df_reset)
