"""
Problem Statement : 53. How to get the last n rows of a dataframe with row sum > 100?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initializing DataFrame 'df'
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print("DataFrame 'df':")
print(df.tail())

# Print row-sum
rowsums = df.apply(np.sum, axis=1)
#print(rowsums)

# Last two rows with row-sum greater than 100
last_two_rows = df.iloc[np.where(rowsums > 100)[0][-2], :]
print(last_two_rows)