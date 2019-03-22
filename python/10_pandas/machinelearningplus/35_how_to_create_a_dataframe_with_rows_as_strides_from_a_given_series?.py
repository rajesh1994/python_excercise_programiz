"""
Problem Statement : 35. How to create a dataframe with rows as strides from a given series?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initialize series1
series1 = pd.Series(range(15))

def gen_strides(a, stride_len = 5, window_len = 5):
	n_strides = ((a.size-window_len)//stride_len) + 1
	return np.array([a[s:(s+window_len)] for s in np.arange(0, a.size, stride_len)[:n_strides]])
print("Create a dataframe with rows as strides from a given series:")
print(gen_strides(series1, stride_len = 2, window_len = 4))
