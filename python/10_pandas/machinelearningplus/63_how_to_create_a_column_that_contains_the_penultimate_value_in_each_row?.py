"""
Problem Statement : 63. How to create a column that contains the penultimate value in each row?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1))
print("DataFrame 'df':")
print(df)

# Create a new column 'penultimate' which has the second largest value of each row of df
out = df.apply(lambda x : x.sort_values().unique()[-2], axis = 1)
df['penultimate'] = out
print("\nColumn 'penultimate' which has the second largest value of each row of df:")
print(df)
