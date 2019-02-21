"""
Problem Statement : How to compute the euclidean distance between two arrays?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'a' & 'b'
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print("Array 'a':")
print(a)
print("\nArray 'b':")
print(b)
# Compute the euclidean distance between two arrays a and b.
euc_dist = np.linalg.norm(a-b)
print("\nEuclidean distance between two arrays a and b:")
print(euc_dist)
