"""
Problem Statement : Extract all odd numbers from 1D array?
"""

# Import numpy as 'np'
import numpy as np

# Creating 1D array
one_d_array = np.arange(10)

# Extracting all odd numbers from 1D array
odd_numbers = one_d_array[one_d_array % 2 == 1]
print("Extracting all odd numbers from 1D array:")
print(odd_numbers)
