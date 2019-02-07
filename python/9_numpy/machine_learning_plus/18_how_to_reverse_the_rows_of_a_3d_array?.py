"""
Problem Statement : How to reverse the rows of a 3D array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# Reverse the rows of a 3D array
print("\nReverse the rows of a 3D array:")
print(x[::-1])
