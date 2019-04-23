"""
Problem Statement : 65. How to compute the correlation of each row with the suceeding row?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
print("DataFrame 'df':")
print(df)

# Correlation of each row of df with its succeeding row
print("\nCorrelation of each row of df with its succeeding row:")
print([df.iloc[i].corr(df.iloc[i + 1]).round(2) for i in range(df.shape[0])[:-1]])
