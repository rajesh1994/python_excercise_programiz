# Numpy's aggregate funtions:

# Import numpy as 'np'
import numpy as np

# Initialize 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# Finding sum of elements using sum() method
sum1 = x.sum()
print("\nSum of the elements:")
print(sum1)

# Finding lowest element from the array using min() method
min1 = x.min()
print("\nLowest element from the array:")
print(min1)
