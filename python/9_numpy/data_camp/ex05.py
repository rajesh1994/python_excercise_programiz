# How NumPy Broadcasting Works

import numpy as np
#Initialize 'x'
x = np.ones((3, 4))

# Check shape of 'x'
print(x.shape)

#Initialize 'y'
y = np.random.random((3, 4))

# Check shape of 'x'
print(x.shape)

print('x = ')
print(x)
print('y = ')
print(y)
# Add 'x' and 'y'
print("x + y = ")
print(x + y)
