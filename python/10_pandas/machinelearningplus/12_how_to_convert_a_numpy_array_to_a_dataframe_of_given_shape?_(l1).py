"""
Problem Statement : 12. How to convert a numpy array to a dataframe of given shape? (L1)
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize numpy array
series1 = pd.Series(np.random.randint(1, 10, 35))
print(series1)

# Reshape the series series1 into a dataframe with 7 rows and 5 columns
df = pd.DataFrame(series1.values.reshape(5, 7))
print("Reshape the series series1 into a dataframe with 7 rows and 5 columns:")
print(df)
