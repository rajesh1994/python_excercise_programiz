"""
Problem Statement : How to find the duplicate records in a numpy array?
"""

# Import numpy as 'np'
import numpy as np

np.random.seed(100)
a  = np.random.randint(1, 5, 10)
print("Array 's' is:")
print(a)

## Solution
# There is no direct function to do this as of 1.13.3

# Create an all True array
out = np.full(a.shape[0], True)

# Find the index position of unique elements
unique_positions = np.unique(a, return_index = True)[1]

# Mark those positions as False
out[unique_positions] = False

print(out)
