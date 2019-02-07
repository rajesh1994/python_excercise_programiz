"""
Problem Statement : How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
"""

# Import numpy as 'np'
import numpy as np

# Create the random array 'x'
x = np.random.seed(100)
sci_not = np.random.random([3, 3])/1e3
np.set_printoptions(suppress = True, precision = 6)
print("numpy array by suppressing the scientific notation (like 1e10) is:")
print(sci_not)
