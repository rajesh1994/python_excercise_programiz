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

# Finding highest element from the array using min() method
max1 = x.max()
print("\nHighest element from the array:")
print(max1)

# Finding mean value of the array using mean() method
mean = x.mean()
print("\nMean value of the array:")
print(mean)
