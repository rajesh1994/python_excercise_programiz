"""
Problem Statement : How to compute the moving average of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

# Compute the moving average of window size 3, for the given 1D array.
def moving_avg(a, n = 3):
    ret = np.cumsum(a, dtype = 'float')
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

# Initialize an array 'a':
np.random.seed(100)
a = np.random.randint(1, 10, 10)
print("Array 'a' is:")
print(a)

# Method 1:
print("\nMethod 1:\nMoving average of array 'a' is:")
print(moving_avg(a, n = 3).round(2))

# Method 2:
print("\nMethod 2:\nMoving average of array 'a' is:")
print(np.convolve(a, np.ones(3)/3, mode = 'valid').round(2))
