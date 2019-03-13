"""
Problem Statement : 18. How to convert the first character of each element in a series to uppercase?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1
series1 = pd.Series(["india", "england", "sri lanka"])
print("Series1:")
print(series1)

# Converting the first character of each element in a series to uppercase
print("\nMethod 1: Converting the first character of each element in a series to uppercase")
print(series1.map(lambda x : x.title()))

print("\nMethod 2: Converting the first character of each element in a series to uppercase")
print(series1.map(lambda x : x[0].upper() + x[1 : ]))

print("\nMethod 3: Converting the first character of each element in a series to uppercase")
print(pd.Series([i.title() for i in series1]))
