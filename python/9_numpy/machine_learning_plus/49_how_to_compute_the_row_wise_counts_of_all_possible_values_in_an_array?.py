"""
Problem Statement : How to compute the row wise counts of all possible values in an array?
"""

# Import numpy as 'np'
import numpy as np

np.random.seed(100)
a = np.random.randint(1, 10, size = (5, 10))
print("Array 'a' is:")
print(a)

# Compute the counts of unique values row-wise
def counts_of_all_values_rowwise(array2d):
    # Unique values & its counts row-wise
    num_counts_array = [np.unique(row, return_counts = True) for row in array2d]
    
    # Counts of all values row-wise
    return([[int(b[a == i])] if i in a else 0 for i in np.unique(array2d) for a, b in num_counts_array])
print("\nCompute the counts of unique values row-wise:")
print([counts_of_all_values_rowwise(a)])
