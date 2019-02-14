"""
Problem Statement : How to replace all values greater than a given value to a given cutoff?
"""

# Import numpy as 'np'
import numpy as np

np.set_printoptions(precision = 2)
np.random.seed(100)
array = np.random.uniform(10, 50, 20)
#print(np.sort(array))

# From the array, replace all values greater than 30 to 30 and less than 10 to 10
# Method 1: By using np.clip()
print("Method 1: By using np.clip():")
print(np.sort(np.clip(array, a_min = 10, a_max = 30)))

# Method 2: By using np.where()
print("\nMethod 2: By using np.where():")
print(np.sort(np.where(array < 10, 10, np.where(array > 30, 30, array))))
