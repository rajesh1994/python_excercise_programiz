"""
Problem Statement : 6.0 Replacing All Occurrences of a String in a DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initializing DataFrame 'df'
df = pd.DataFrame(data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index = [1, 2, 3], columns = ['A', 'B', 'C'])
print("DataFrame 'df' is:")
print(df)

# Replacing value 1 by 10 based on index
print("\nReplacing values 1 by 10:")
print(df.replace([1], [10]))

# Replacing value 2 by 20 based on index
print("\nReplacing values 2 by 20:")
print(df.replace([2], [20]))

# Replacing values 1, 4, 7 by 100, 400, 700 respectively based on values & column name
print("\nReplacing values 1, 4, 7 by 100, 400, 700 respectively:")
print(df.replace({'A' : {1 : 100, 4 : 400, 7 : 700}}))

# Replacing values 7, 8, 9 by 700, 800, 900 respectively based on values
print("\nReplacing values 7, 8, 9 by 700, 800, 900 respectively:")
print(df.replace([7], [700]).replace([8], [800]).replace([9], [900]))
