"""
Problem Statement : How to create strides from a given 1D array?
"""

# Import numpy as 'np'
import numpy as np

# Initialize an array 'x'
x = np.arange(15)
print("Array 'x' is:")
print(x)

def gen_strides(x, stride_len = 5, window_len = 5):
    n_strides = ((x.size-window_len)//stride_len) + 1
    return np.array([x[s:(s+window_len)] for s in np.arange(0, n_strides * stride_len, stride_len)])
print("\n2d array from 1d array using strides:")
print(gen_strides(x, stride_len = 2, window_len = 4))
