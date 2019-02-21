"""
Problem Statement : How to subtract a 1d array from a 2d array, where each item of 1d array subtracts from respective row?
"""

# Import numpy as 'np'
import numpy as np

# Initialize 1d & 2d array:
a = np.array([1, 2, 3, 4])
b = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]])
print("Array 'a':")
print(a)
print("\nArray 'b':")
print(b)
# Subtract the 1d array a_1d from the 2d array a_2d, such that each item of a_1d subtracts from respective row of a_2d.
print("\nSubtract the 1d array from the 2d array:")
print(b - a[:,None])
