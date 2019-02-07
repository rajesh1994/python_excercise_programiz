"""
Problem Statement : How to print the full numpy array without truncating
"""

# Import numpy as 'np'
import numpy as np

np.set_printoptions(threshold = 6)

# Initialize array 'x'
x = np.arange(15)
print("Array 'x' is:")
np.set_printoptions(threshold = np.nan)
print(x)
