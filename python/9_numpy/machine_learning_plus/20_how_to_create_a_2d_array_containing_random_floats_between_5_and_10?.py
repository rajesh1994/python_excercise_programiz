"""
Problem Statement : How to create a 3D array containing random floats between 5 and 10?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# 3D array containing random floats between 5 and 10
# Method 1: By using random.randint() method
random_float1 = np.random.randint(low = 1, high = 10, size = (5, 3)) + np.random.random((5, 3))
print("\nMethod 1: By using random.randint() method:\n3D array containing random floats between 5 and 10:")
print(random_float1)

# Method 2: By using random.uniform() method
random_float2 = np.random.uniform(5, 10, size = (5, 3))
print("\nMethod 2: By using random.uniform() method:\n3D array containing random floats between 5 and 10:")
print(random_float2)
