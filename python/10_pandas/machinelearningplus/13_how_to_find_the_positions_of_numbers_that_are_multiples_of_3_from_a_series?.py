"""
Problem Statement : 13. How to find the positions of numbers that are multiples of 3 from a series?
"""

# Import numpy as np
# Import pandads as pd
import numpy as np
import pandas as pd

# Initalize series1
series1 = pd.Series(np.random.randint(1, 10, 7))
print("series1:")
print(series1)

# Finding the numbers that are multiples of 3 from a series
print("Finding the numbers that are multiples of 3 from a series:")
print(np.argwhere(series1 % 3 == 0))
