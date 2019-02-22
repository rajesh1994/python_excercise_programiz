"""
Problem Statement : How to create a numpy array sequence given only the starting point, length and the step?
"""

# Import numpy as 'np'
import numpy as np

# Create a numpy array of length 10, starting from 5 and has a step of 3 between consecutive numbers.
length = int(input("Enter the length of the numpy array :"))
start = int(input("\nEnter the starting poition of numpy array :"))
step = int(input("\nEnter the step value :"))

def seq(start, length, step):
    end = start + (length * step)
    return np.arange(start, end, step)
print("\nNumpy array sequence:")
print(seq(start, length, step))
