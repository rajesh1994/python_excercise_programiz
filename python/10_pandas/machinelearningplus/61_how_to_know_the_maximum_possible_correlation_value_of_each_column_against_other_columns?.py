"""
Problem Statement : 61. How to know the maximum possible correlation value of each column against other columns?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 80).reshape(8, -1), columns = list('pqrstuvwxy'), index = list('abcdefgh'))
print("DataFrame 'df':")
print(df)

# Maximum possible correlation value of each column against other columns
df_abs_corr = np.abs(df.corr())
#print(df_abs_corr)
max_corr = df_abs_corr.apply(lambda x : sorted(x)[-2])
print("\nMaximum Correlation possible for each column:")
print(np.round(max_corr, 2))
