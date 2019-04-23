"""
Problem Statement : 59. Which column contains the highest number of row-wise maximum values?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1))
print("DataFrame 'df':")
print(df)

# Column with highest row maxes
print("\nColumn with highest row maxes:")
print(df.apply(np.argmax, axis = 1).value_counts().index[0])
