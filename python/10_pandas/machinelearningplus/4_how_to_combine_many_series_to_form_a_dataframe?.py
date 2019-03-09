"""
Problem Statement : 4. How to combine many series to form a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initalizing series1 , series2
series1 = pd.Series(list("abcedfghijklmnopqrstuvwxyz"))
series2 = pd.Series(np.arange(26))

# Method 1 : Combining many Series to form a DataFrame
print("Method 1 : Combining many Series to form a DataFrame")
print(pd.concat([series1, series2], axis = 1).head())

# Method 2 : Combining many Series to form a DataFrame
print("\nMethod 2 : Combining many Series to form a DataFrame")
print(pd.DataFrame({'col1' : series1, 'col2' : series2}).head())
