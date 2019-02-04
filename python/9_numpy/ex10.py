# Numpy's logical operations

# Import numpy as 'np'
import numpy as np

# Initialize 'x' & 'y'
x = np.array([[0, True, False], [7, 8, 22], [44, 22, 38]])
y = np.array([[19, 7, 5], [37, 31, 83], [26, 53, 101]])

# Print 'x' & 'y'
print("Array of 'x' is:")
print(x)
print("\nArray of 'y' is:")
print(y)

# Logical OR operation in an array using np.logical_or() method
or1 = np.logical_or(x, y)
print("\nLogical OR operation in an array 'x' & 'y':")
print(or1)

# Logical AND operation in an array using np.logical_and() method
and1 = np.logical_and(x, y)
print("\nLogical AND operations in an array 'x' & 'y':")
print(and1)

# Logical NOT operation in an array using np.logical_not() method
not1 = np.logical_not(x, y)
print("\nLogical NOT operation in an array 'x' & 'y':")
print(not1)
