"""
Problem Statement : How to generate custom sequences in numpy without hardcoding?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.array([1, 2, 3])
print("Array 'x' is:")
print(x)

# Generating custom sequence using repeat() & tile() method
custom_seq = np.r_[np.repeat(x, 3), np.tile(x, 3)]
print("\nGenerated custom sequence:")
print(custom_seq)
