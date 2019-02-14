"""
Problem Statement : How to get the positions of top n values from a numpy array?
"""

# Import numpy as 'np'
import numpy as np

np.set_printoptions(precision = 2)
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
#print(array)

# Get the positions of top 5 maximum values in a given array a.

# Solution 1:
print("Solution 1:")
print(a.argsort())

# Solution 2:
print("\nSolution 2:")
print(np.argpartition(-a, 5)[:5])

# 
