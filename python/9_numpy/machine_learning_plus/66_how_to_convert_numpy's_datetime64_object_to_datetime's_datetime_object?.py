"""
Problem Statement : How to convert numpy's datetime64 object to datetime's datetime object?
"""

# Import numpy as 'np'
import numpy as np

# Input : A numpy datetime64 object
dt64 = np.datetime64('2018-02-25 22:10:10')

# Convert numpy's datetime64 object to datetime's datetime object

# Solution 1: By using tolist() method
from datetime import datetime
date1 = dt64.tolist()
print("Solution 1: By using tolist() method:")
print(date1)

# Solution 2: By using astype() method
date2 = dt64.astype(datetime)
print("\nSolution 2: By using date2() astype:")
print(date2)
