"""
Problem Statement : 69. How to compute grouped mean on pandas dataframe and keep the grouped column as another column (not index)?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame({'fruits' : ['apple', 'banana', 'orange'] * 3, 'rating' : np.random.rand(9), 'price' : np.random.randint(1, 15, 9)})
print("DataFrame 'df':")
print(df)

# In df, Compute the mean price of every fruit, while keeping the fruit as another column instead of an index
df_out = df.groupby('fruits', as_index = 0)['price'].mean()
print("\nMean price of every fruit, while keeping the fruit as another column instead of an index:")
print(df_out)
