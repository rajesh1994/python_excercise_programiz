"""
Problem Statement : 4.0 How to Delete Indices From a Pandas Data Frame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), index = [2.1, 3.2, 3.6, 6.3, 3.2], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

print(df.reset_index().drop_duplicates(subset = 'index', keep = 'last').set_index('index'))
