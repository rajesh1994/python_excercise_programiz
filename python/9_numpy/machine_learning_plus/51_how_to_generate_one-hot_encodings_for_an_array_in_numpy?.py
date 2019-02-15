"""
Problem Statement : How to generate one-hot encodings for an array in numpy?
"""

# Import numpy as 'np'
import numpy as np

np.random.seed(100)
a = np.random.randint(1, 4, size = 6)
print("Array 'a' is:")
print(a)

# Compute the one-hot encodings (dummy binary variables for each unique value in the array)
print("Method 1:\nGenerating one-hot encodings for an array 'a':")
print((a[:, None] == np.unique(a)).view(np.int8))
