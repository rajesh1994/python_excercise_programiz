"""
Problem Statement : 1. How to create a boolean array?
                    2. Create a 3×3 numpy array of all True
"""

# Import numpy as np
import numpy as np

# Method 1
# Creating a boolean array by using np.full() method
bool_array1 = np.full((3, 3), True, dtype = bool)

# Printing a (3 x 3) boolean array
print("Printing a 3x3 boolean array by using np.full() method:")
print(bool_array1)

# Method 2
# Creating a boolean array by using np.ones() method
bool_array2 = np.ones((3, 3), dtype = bool)

# Printing a (3 x 3) boolean array
print("\nPrinting a 3x3 boolean array by using np.ones() method:")
print(bool_array2)
