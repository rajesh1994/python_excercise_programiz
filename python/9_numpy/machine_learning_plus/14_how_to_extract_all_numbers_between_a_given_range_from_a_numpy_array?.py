"""
Problem Statement : How to extract all numbers between a given range from a numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.arange(15)
print("Array 'x' is:")
print(x)

# Method 1
# Get all items between 5 and 10 from x
index1 = np.where((x >= 5) & (x <= 10))
print("\nFetching all items between 5 and 10 from x:")
print(x[index1])

# Method 2
# Get all items between 5 and 10 from x
index2 = np.where(np.logical_and(x >= 5, x <= 10))
print("\nFetching all items between 5 and 10 from x:")
print(index2)
