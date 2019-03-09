"""
Problem Statement : 5. How to assign name to the series index?
"""
# Import pandas as pd
import pandas as pd

# Initializing Series
series1 = pd.Series(list("abcedfghijklmnopqrstuvwxyz"))

# Assign name to the series index as 'alphabets'
series1.name = "alphabets"
print("Assign name to the series index as 'alphabets':")
print(series1.head())
