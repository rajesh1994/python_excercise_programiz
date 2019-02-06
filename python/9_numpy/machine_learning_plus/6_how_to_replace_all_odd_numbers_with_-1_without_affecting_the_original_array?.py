"""
Problem Statement : How to replace all odd numbers with -1 without affecting the original array?
"""

# Import numpy as 'np'
import numpy as np

# Initializing 1D array
x = np.arange(10)
print("Original array:")
print(x)

# Replace all odd numbers with -1 without affecting the original array
y = np.where(x % 2 == 1, -1, x)
print("\nModified array:")
print(y)

