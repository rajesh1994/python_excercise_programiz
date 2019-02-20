"""
Problem Statement : How to drop all missing values from a numpy array?
"""

# Import numpy as 'np'
import numpy as np

a = np.array([1, 2, np.nan, 4, 5, np.nan, 7, np.nan, 9, 10, np.nan])
print("Array 'a' is:")
print(a)

# Drop all nan values from a 1D numpy array
print("\nAfter droping missing values in array 'a' is:")
print(a[~np.isnan(a)])
