"""
Problem Statement : How to get the common items between two python numpy arrays?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x' & 'y'
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)

# Fetching common items between arrays 'x' & 'y'
common_items = np.intersect1d(x, y)
print("\nCommon items between arrays 'x' & 'y' are:")
print(common_items)
