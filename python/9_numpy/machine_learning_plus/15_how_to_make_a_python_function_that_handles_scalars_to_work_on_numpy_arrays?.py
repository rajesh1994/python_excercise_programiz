"""
Problem Statement : How to make a python function that handles scalars to work on numpy arrays?
"""

# Import numpy as 'np'
import numpy as np

def max1(x, y):
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(max1, otypes = [float])

# Initialize array 'x' & 'y'
x = np.array([12, 3, 18, 22, 35, 88, 100, 84, 23, 44, 56])
y = np.array([2, 34, 44, 91, 23, 102, 73, 42, 61, 56, 102])
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)
print("\nGreater elements between arrays 'x' & 'y':")
print(pair_max(x, y))
