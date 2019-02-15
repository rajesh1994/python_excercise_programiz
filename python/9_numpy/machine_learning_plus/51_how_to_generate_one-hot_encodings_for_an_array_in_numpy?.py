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
print("Generating one-hot encodings for an array 'a':")
print(a[:, None] == np.unique(a)).view(int8)
#(arr[:, None] == np.unique(arr)).view(np.int8)
