# How To Make An “Empty” NumPy Array
import numpy as np

# Create an array of ones
a1 = np.ones((3, 5))
print("Creating an array of ones:")
print(a1)

# Create an array of zeros
a2 = np.zeros((2, 3, 4), dtype = np.int16)
print("\nCreating an array of zeros:")
print(a2)

# Create an array with random values
a3 = np.random.random((2, 2))
print("\nCreating an array with random values:")
print (a3)

# Create an empty array
a4 = np.empty((2, 3))
print("\nCreating an empty array:")
print(a4)

# Create a full array
a5 = np.full((2, 2), 7, dtype = np.int16)
print("\nCreating a full array:")
print(a5)

# Create an array of evenly placed value
a6 = np.arange(0, 100, 5)
print("\nCreating an array of evenly placed value:")
print(a6)

# Create an array of evenly placed value
a7 = np.linspace(0, 1, 9)
print("\nCreating an array of evenly placed value:")
print(a7)
