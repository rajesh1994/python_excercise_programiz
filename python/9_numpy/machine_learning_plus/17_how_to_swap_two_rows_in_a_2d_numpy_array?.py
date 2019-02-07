"""
Problem Statement : How to swap two rows in a 3D numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# Swap two rows in a 3D numpy array
row_swap = x[[1, 0, 2], :]
print("\nSwap two rows in a 2D numpy array:")
print(row_swap)
