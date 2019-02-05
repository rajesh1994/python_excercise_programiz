# How To Join And Split Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x', 'y', 'my_resized_array' and 'my_2d_array'
x = np.array([[10, 20]])
y = np.array([[30, 40]])
my_2d_array = np.array([[22, 11], [33, 44]])

# Concatenate array 'x' & 'y'
print("Concatenate array 'x' & 'y':")
print(np.concatenate(x, y))

# Stack arrays row-wise
print("Stack arrays row-wise:")
print(np.vstack((y, my_2d_array)))
