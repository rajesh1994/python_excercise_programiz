"""
Problem Statement : 9.0 How To Iterate Over a Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize 'df' DataFrame
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]]), columns = ['A', 'B', 'C'])
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Iterating rows 'A' & 'B' from 'df' DataFrame
print("\nRows 'A' & 'B' from 'df' DataFrame are:")
for index, row in df.iterrows():
	print(row['A'], row['B'])
