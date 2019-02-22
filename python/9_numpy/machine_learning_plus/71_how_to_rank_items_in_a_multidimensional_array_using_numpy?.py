"""
Problem Statement : How to rank items in a multidimensional array using numpy?
"""

# Import numpy as 'np'
import numpy as np

# Create a rank array of the same shape as a given numeric array a.
np.random.seed(10)
a = np.random.randint(20, size = [2, 5])
print("Array 'a' is:")
print(a)
print("\nRank items in a multidimensional array:")
print(a.ravel().argsort().argsort().reshape(a.shape))
