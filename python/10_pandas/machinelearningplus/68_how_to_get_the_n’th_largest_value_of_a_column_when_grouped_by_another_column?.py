"""
Problem Statement : 68. How to get the n’th largest value of a column when grouped by another column?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame({'fruits' : ['apple', 'banana', 'orange'] * 3, 'taste' : np.random.rand(9), 'price' : np.random.randint(0, 15, 9)})
print("DataFrame 'df':")
print(df)

# In df, find the second largest value of 'taste' for 'banana'
df_grouped = df['taste'].groupby(df.fruits)
print("\nIn df, find the second largest value of 'taste' for 'banana':")
print(df_grouped.get_group('banana').sort_values().iloc[-2])
