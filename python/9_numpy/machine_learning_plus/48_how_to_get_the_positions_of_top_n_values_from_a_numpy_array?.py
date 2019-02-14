"""
Problem Statement : How to get the positions of top n values from a numpy array?
"""

# Import numpy as 'np'
import numpy as np

np.set_printoptions(precision = 2)
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print("Array 'a' is:")
print(np.sort(a))

# Get the positions of top 5 maximum values in a given array a.

# Solution 1:
print("\nSolution 1:")
print(np.argpartition(-a, 5)[:5])

# Below methods will get you the values

# Method 1:
print("\nMethod 1:")
print(a[a.argsort()][-5:])

# Method 2:
print("\nMethod 2:")
print(np.sort(a)[-5:])

# Method 3:
print("\nMethod 3:")
print(np.partition(a, kth = -5)[-5:])
#np.partition(a, kth=-5)[-5:]

# Method 4:
print("\nMethod 4:")
print(np.argpartition(-a, 5)[:5])
