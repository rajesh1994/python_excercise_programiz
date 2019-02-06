"""
Problem Statement : How to remove from one array those items that exist in another?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x' & 'y'
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)

# Remove from one array those items that exist in another
unique_items = np.setdiff1d(x, y)
print("\nAfter remove from one array those items that exist in another:")
print(unique_items)
