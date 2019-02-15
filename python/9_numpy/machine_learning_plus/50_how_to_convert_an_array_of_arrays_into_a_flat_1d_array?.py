"""
Problem Statement : How to convert an array of arrays into a flat 1d array?
"""

# Import numpy as 'np'
import numpy as np

a1 = np.arange(3)
a2 = np.arange(3, 7)
a3 = np.arange(7, 10)
array_of_arrays = np.array([a1, a2, a3])
print("Array of arrays:")
print(array_of_arrays)

# Solution 1: By using np.concatenate()
array_2d1 = np.concatenate(array_of_arrays)
print("Solution 1: By using np.concatenate():")
print(array_2d1)

# Solution 2: By using np.array()
array_2d2 = np.array(np.array([a for arr in array_of_arrays for a in arr]))
print("\nSolution 2: By using np.array():")
print(array_2d2)
