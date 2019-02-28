"""
Problem Statement : 6.0 Removing Parts From Strings in the Cells of Your DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = np.array([[1, 2, '+3b'], [4, 5, '-6b'], [7, 8, '+9A']]), index = [1, 2, 3], columns = ['class', 'test', 'result'])
print("DataFrame 'df' is:")
print(df)

# Delete unwanted parts from the strings in the result column
print("\nDelete unwanted parts from the strings in the result column:")
df['result'] = df['result'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
print(df)
