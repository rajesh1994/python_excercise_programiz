# How To Join And Split Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x', 'y', 'my_resized_array' and 'my_2d_array'
x = np.array([[10, 20]])
y = np.array([[30, 40]])
my_2d_array = np.array([[22, 11], [33, 44]])
my_resized_array = np.array([[7, 6], [20, 27]])

# Printing array 'x', 'y', 'my_2d_array & 'my_resized_array'
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)
print("\nArray 'my_2d_array' is:")
print(my_2d_array)
print("\nArray 'my_resized_array' is:")
print(my_resized_array)
# Concatenate array 'x' & 'y'
print("\nConcatenate array 'x' & 'y':")
print(np.concatenate((x, y)))

# Stack arrays row-wise
print("\nStack arrays y, my_2d_array as row-wise:")
print(np.vstack((y, my_2d_array)))

# Stack arrays row-wise
print("\nStack arrays my_resized_array, my_2d_array as row-wise:")
print(np.r_[my_resized_array, my_2d_array])

# Stack arrays column-wise
print("\nStack arrays my_resized_array, my_2d_array as column-wise:")
print(np.column_stack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print("\nStack arrays my_resized_array, my_2d_array as column-wise:")
print(np.c_[my_resized_array, my_2d_array])

# Stack arrays horizontally
print("\nStack arrays my_resized_array, my_2d_array as horizontally:")
print(np.hstack((my_resized_array, my_2d_array)))

# Split array 'my_2d_array' horizontally at the 1st index
print("\nSplit 'my_2d_array' horizontally at the 2nd index:")
print(np.hsplit(my_2d_array, 2))

# Split array 'my_2d_array' vertically at the 1st index
print("\nSplit 'my_2d_array' horizontally at the 2nd index:")
print(np.vsplit(my_2d_array, 2))
