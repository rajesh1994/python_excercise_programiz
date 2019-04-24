"""
Problem Statement : 72. How to create lags and leads of a column in a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame({'fruit1' : np.random.choice(['apple', 'banana', 'orange'], 10), 'fruit2' : np.random.choice(['apple', 'banana', 'orange'], 10)})
print("DataFrame 'df':")
print(df)

# Positions of where values of two columns match
print("\nPositions of where values of two columns match:")
print(np.where(df.fruit1 == df.fruit2))
