"""
Problem Statement : 1. How to create a boolean array?
                    2. Create a 3×3 numpy array of all True
"""

# Import numpy as np
import numpy as np

# Method 1
# Creating a boolean array bu using np.full() method
bool_array1 = np.full((3, 3), True, dtype = bool)

# Printing a (3 x 3) boolean array
print("Printing a (3 x 3) boolean array")
print(bool_array)

# Method 2
# Creating a boolean array bu using np.ones() method
bool_array2 = np.ones((3, 3), dtype = bool)

# Printing a (3 x 3) boolean array
print("Printing a (3 x 3) boolean array")
print(bool_array2)
