"""
Problem Statement : How to rank items in an array using numpy?
"""

# Import numpy as 'np'
import numpy as np

np.random.seed(100)
a = np.random.randint(20, size = 20)
print("Array 'a':")
print(a)
print("\nRank items in an array:")
print(a.argsort().argsort())
