"""
Problem Statement : How to find all the local maxima (or peaks) in a 1d array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'a':
a = np.array([8, 10, 1, 4, 0, 6, 2, 7, 11, 101, 3])
print("Array 'a' is:")
print(a)

# Find all the peaks in a 1D numpy array a. Peaks are points surrounded by smaller values on both sides.
double_diff = np.diff(np.sign(np.diff(a)))
peak_location = np.where(double_diff == -2)[0] + 1
print("\nLocal maxima in array 'a':")
print(peak_location)
