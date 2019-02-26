"""
Problem Statement : 3.0 How To Add an Index to a Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['A', 'B', 'C'])
print("DataFrame 'np' is:")
print(df)

# Setting 'C' as the index to DataFrame 'df'
print("\nSetting 'C' as the index to DataFrame 'df':")
print(df.set_index('C'))
