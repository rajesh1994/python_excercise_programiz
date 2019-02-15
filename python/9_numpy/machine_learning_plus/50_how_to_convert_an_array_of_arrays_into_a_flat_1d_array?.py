"""
Problem Statement : How to convert an array of arrays into a flat 1d array?
"""

# Import numpy as 'np'
import numpy as np

a1 = np.arange(3)
a2 = np.arange(3, 7)
a3 = np.arange(7, 10)
arrays_of_array = np.array([a1, a2, a3])
print("Arrays of array:")
print(arrays_of_array)

# Solution 1: By using np.concatenate()
array_2d = np.concatenate(arrays_of_array)
