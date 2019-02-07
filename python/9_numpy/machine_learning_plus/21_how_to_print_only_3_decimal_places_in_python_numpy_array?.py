"""
Problem Statement : How to print only 3 decimal places in python numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Print only 3 decimal places in python numpy array
x = np.random.randint(low = 1, high = 20, size = (3, 3)) + np.random.random([3, 3])
np.set_printoptions(precision = 3)
print("Print only 3 decimal places in python numpy array:")
print(x)
