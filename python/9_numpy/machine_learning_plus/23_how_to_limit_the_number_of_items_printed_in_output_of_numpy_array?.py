"""
Problem Statement : How to limit the number of items printed in output of numpy array?
"""

# Import numpy as 'np'
import numpy as np
np.set_printoptions(threshold = -1)
# Initialize array 'x'
x = np.arange(15)
print("Array 'x' is:")
print(x)

# Setting the threshold for number of items printed in output of numpy array
