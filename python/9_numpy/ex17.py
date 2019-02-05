# How To Join And Split Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x', 'y', 'my_resized_array' and 'my_2d_array'
x = np.array([[10, 20]])
y = np.array([[30, 40]])
my_2d_array = np.array([[22, 11], [33, 44]])

# Printing array 'x', 'y', 'my_2d_array
 print("Array 'x' is:")
 print(x)
 print("\nArray 'y' is:")
 print(y)
 print("\nArray 'my_2d_array' is:")
# Concatenate array 'x' & 'y'
print("\nConcatenate array 'x' & 'y':")
print(np.concatenate((x, y)))

# Stack arrays row-wise
print("\nStack arrays row-wise:")
print(np.vstack((y, my_2d_array)))
