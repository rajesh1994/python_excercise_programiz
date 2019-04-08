"""
Problem Statement : 52. How to find the position of the nth largest value greater than a given value?
"""

# Import numpy as np
# Import pandasa as pd
import numpy as np
import pandas as pd

# Defining a Series 's'
s = pd.Series(np.random.randint(1, 100, 15))
print("Series 's':")
print(s.tolist())

# In ser, find the position of the 2nd largest value greater than the mean.
print("\nMean of the Series:")
print(round(s.mean()))
print("Position of the 2nd largest value greater than the mean is:")
print(np.argwhere(s > s.mean())[1])
