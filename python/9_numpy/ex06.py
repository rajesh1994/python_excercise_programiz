# Adding & Subtracting 2D array with 1D array

#import numpy as 'np'
import numpy as np

# Initialize 'x'
x = np.ones((3, 4))
print("array x is:")
print(x)
print("Shape of x is:", x.shape)

# Initialize 'y'
y = np.arange(4)
print("array y is:")
print(y)
print("Shape of y is:", y.shape)

# Adding 'x' & 'y'
print("Addition of two arrays:")
print(x + y)

# Subtracting 'x' & 'y'
print("Subtraction of two arrays:")
print(x - y)
