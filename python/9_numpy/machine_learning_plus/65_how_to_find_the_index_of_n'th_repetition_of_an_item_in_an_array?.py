"""
Problem Statement : How to find the index of n'th repetition of an item in an array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5
# Find the index of 5th repetition of number 1 in x.

# Solution 1: By using list comprehension
repet1 = [i for i, v in enumerate(x) if v == 1][n - 1]
print("\nSolution 1: By using list comprehension:")
print(repet1)

# Solution 2: By using numpy version
repet2 = np.where(x == 1)[0][n - 1]
print("\nSolution 2: By using numpy version:")
print(repet2)
