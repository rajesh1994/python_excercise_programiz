"""
Problem Statement : 73. How to get the frequency of unique values in the entire dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
print("DataFrame 'df':")
print(df)

# Frequency of unique values in the entire dataframe
print("\nFrequency of unique values in the entire dataframe:")
print(pd.value_counts(df.values.ravel()))
