"""
Problem Statement : 3.1 How To Add a Row or Column to a Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Adding a column to a DataFrame
df['D'] = df.index

print("After adding column 'D' to Data")
print(df)
