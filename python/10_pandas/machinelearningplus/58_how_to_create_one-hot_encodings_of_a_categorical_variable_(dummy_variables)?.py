"""
Problem Statement : 58. How to create one-hot encodings of a categorical variable (dummy variables)?
"""

# Import numpy as np
# Import pandas as pd
import pandas as pd
import numpy as np

# Initialize DataFrame 'df'
df = pd.DataFrame(np.arange(25).reshape(5, -1), columns = list('abcde'))
print("DataFrame 'df':")
print(df)

# Create one-hot encodings of a categorical variable (dummy variables)
df_onehot = pd.concat([pd.get_dummies(df['a']), df[list('bcde')]], axis = 1)
print("\nCreate one-hot encodings of a categorical variable(dummy variables):")
print(df_onehot)
