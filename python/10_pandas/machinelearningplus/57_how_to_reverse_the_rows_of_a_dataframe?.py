"""
Problem Statement : 57. How to reverse the rows of a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.arange(25).reshape(5, -1))
print("DataFrame 'df':")
print(df)

# Reverse the rows of a DataFrame
print("\nReverse the rows of a DataFrame:")
print(df.iloc[:: -1, :])
