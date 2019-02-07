"""
Problem Statement : How to swap two columns in a 2d numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# Swap two columns in a 2D numpy array
column_swap = x[:, [1, 0, 2]]
print("\nTwo columns swapped in a 2d numpy array:")
print(column_swap)
