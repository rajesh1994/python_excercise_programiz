# How To Transpose Your Arrays

# Importing numpy as 'np'
import numpy as np

# Initialize array 'x' & 'y'
x = np.array([[2, 4, 5, 8, 7], [10, 13, 28, 26, 37], [44, 32, 20, 88, 31]])
y = np.array([[10, 13, 28, 26, 37], [44, 32, 20, 88, 31], [2, 4, 5, 8, 7]])
# Printing an array 'x'
print("Array 'x' is:")
print(x)
print("Array 'y' is:")
print(y)

# Tranpose an array 'x' by using transpose() method
print("\nTranpose an array 'x' by using transpose() method:")
print(np.transpose(x))

# Tranpose an array 'y' by using keyword 'T'
print("\nTranpose an array 'y' by using keyword 'T'")
print(y.T)
