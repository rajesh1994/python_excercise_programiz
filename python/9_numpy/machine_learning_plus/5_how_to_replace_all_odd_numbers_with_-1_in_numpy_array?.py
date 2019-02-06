"""
Problem Statement : How to replace all odd numbers with -1 in numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Creating 1D array
one_d_array = np.arange(10)
# Printing 1D array
print("1D array is:")
print(one_d_array)

# Replace all odd numbers with -1
one_d_array[one_d_array % 2 == 1] = -1
print("\nReplace all odd numbers with -1:")
print(one_d_array)
