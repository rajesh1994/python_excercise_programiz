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

# Method 1 using vstack() method
vertical1  = np.vstack([x, y])
print("\nMethod 1 using vstack() method:")
print(vertical1)

# Method 2 using r_() method
vertical2 = np.r_[x, y]
print("\nMethod 2 using r_() method:")
print(vertical2)

# Method 3 using concatenate() method
vertical3 = np.concatenate([x, y], axis = 0)
print("\nMethod 3 using concatenate() method:")
print(vertical3)
