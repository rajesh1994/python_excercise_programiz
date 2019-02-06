"""
Problem Statement : How to get the positions where elements of two arrays match?
"""

# Import numpy as 'np'
import numpy as np

# Initialze array 'x' & 'y'
x = np.array([22, 30, 45, 29, 100, 26, 103, 78, 11, 16, 19])
y = np.array([89, 30, 22, 29, 104, 26, 101, 78, 12, 16, 20])
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)

# Fetching the positions where elements of two arrays match
match = np.where(x == y)
print("\nThe positions where elements of two arrays match:")
print(match)
