# Reshaping Versus Resizing Your Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print("Array 'x' is:")
print(x)

# Print the shape of 'x'
print("\nThe shape of the array 'x' is:", x.shape)

# Resize 'x' to (5, 3)
print("\nResize 'x' to (5, 3):")
print(np.resize(x, (5, 3)))

# Initialize array 'y'
y = np.array([[10, 23, 34, 23], [21, 12, 33, 23], [11, 22, 33, 44]])
print("\nArray 'y' is:")
print(y)

# Print the shape of 'y'
print("\nShape of the array 'y' is:", y.shape)

# Reshape 'y' to (4, 3)
print("\nReshaping to 'y' to (4, 3)")
print(np.reshape(y, (4, 3)))
