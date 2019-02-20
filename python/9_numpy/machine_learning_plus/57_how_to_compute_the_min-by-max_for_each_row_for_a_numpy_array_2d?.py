"""
Problem Statement : How to compute the min-by-max for each row for a numpy array 2d?
"""

# Import numpy as 'np'
import numpy as np

np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])
print("Array 'a' is:")
print(a)
# Compute the min-by-max for each row for given 2d numpy array.
print("\nMin-by-max for each row for a numpy array 2d:")
print(np.apply_along_axis(lambda x: np.min(x)/np.max(x), arr = a, axis = 1))
