"""
Problem Statement : How to stack two arrays horizontally?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x' & 'y'
x = np.arange(10).reshape(2, -1)
y = np.ones(10).reshape(2, -1)
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)

# Method 1 using hstack() method
horizontal1 = np.hstack([x, y])
print("\nMethod 1 using hstack() method:")
print(horizontal1)

# Method 1 using c_() method
horizontal2 = np.c_[x, y]
print("\nMethod 2 using c_() method:")
print(horizontal2)

# Method 1 using concatenate() method
horizontal3 = np.concatenate([x, y], axis = 1)
print("\nMethod 3 using concatenate() method:")
print(horizontal3)
