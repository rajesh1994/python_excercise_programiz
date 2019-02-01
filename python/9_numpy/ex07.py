# The arrays can only be broadcast together if they are compatible in all dimensions
# Consider the following example:

# Import numpy as 'np'
import numpy as np

# Initialize 'x' & 'y'
x = np.array((3, 4))
y = np.random.random((5, 1, 4))

# Add 'x' & 'y'
print("Addition of 'x' & 'y':")
print(x + y)
