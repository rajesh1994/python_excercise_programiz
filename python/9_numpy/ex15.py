# How To Append Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x1'
x1 = np.array([[7, 5, 9, 3], [2, 3, 4, 5]])
print("Array 'x1' is:")
print(x1)

# Appending 1D array to array 'x1'
x2 = np.append(x1, [12, 14, 16, 18])
print("\nAfter appending 1D array to array x1:")
print(x2)

# Initialize array 'y1'
y1 = np.array([[2,3], [4, 5]])
print("\nArray 'y1' is:")
print(y1)

# Appending an extra colomn to array y1
y2 = np.append(y1, [[8], [6]], axis = 1)
print("\nAfter appending an extra colomn to array y1:")
print(y2)
