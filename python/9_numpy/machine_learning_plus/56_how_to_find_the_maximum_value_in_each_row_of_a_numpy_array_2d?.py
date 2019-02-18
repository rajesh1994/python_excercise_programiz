"""
Problem Statement : How to find the maximum value in each row of a numpy array 2d?
"""

# Import numpy as 'np'
import numpy as np

# Compute the maximum for each row in the given array.
np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])
print("Array 'a' is:")
print(a)

# Method 1: By using np.amax() method
print("\nMethod 1:\nMaximum value in each row of an array:")
print(np.amax(a, axis = 1))

# Method 2: By using np.apply_along_axis() method
print("\nMethod 2:\nMaximum value in each of an array:")
print(np.apply_along_axis(np.max, arr = a, axis = 1))
