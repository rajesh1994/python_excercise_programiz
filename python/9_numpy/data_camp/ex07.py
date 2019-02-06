# The arrays can only be broadcast together if they are compatible in all dimensions
# Consider the following example:

# Import numpy as 'np'
import numpy as np

# Initialize 'x' & 'y'
x = np.ones((3, 4))
y = np.random.random((5, 1, 4))
print("Array x:")
print(x)
print("\nShape of x:", x.shape)
print("\nArray y:")
print(y)

# Add 'x' & 'y'
print("\nAddition of 'x' & 'y':")
print(x + y)
