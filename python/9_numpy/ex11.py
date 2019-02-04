# How To Subset, Slice, And Index Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.array([[20, 34, 12, 46], [45, 32, 19, 10], [67, 83, 20, 20]])

# Printing an array 'x'
print("Array 'x' is:")
print(x)

# Numpy's subsetting examples

# Select the element at the 1st index
print("\nPrinting the element at the 1st index:")
print(x[1])

# Method 1
# Select the element at row 1 colomn 2
print("\nPrinting the element at row 1 coloumn 2:")
print(x[1][2])

# Method 2
# Select the element at row 1 colomn 2
print("\nPrinting the element at row 1 colomn 2:")
print(x[1, 2])
