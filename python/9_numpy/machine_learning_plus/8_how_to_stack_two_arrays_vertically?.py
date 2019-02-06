"""
Problem Statement : How to stack two arrays vertically?
"""

# Import numpy as 'np'
import numpy as np

# Initialize arrays 'x' & 'y'
x = np.arange(10).reshape(2, -1)
y = np.repeat(1, 10).reshape(2, -1)
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)
