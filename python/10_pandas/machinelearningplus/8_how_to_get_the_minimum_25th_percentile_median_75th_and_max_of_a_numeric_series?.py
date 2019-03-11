"""
Problem Statement : 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initilize series1
state = np.random.RandomState(100)
series1 = pd.Series(state.normal(10, 5, 25))

# Getting the minimum, 25th percentile, median, 75th percentile & maximum of a numeric series
series2 = np.percentile(series1, q = [0, 25, 50, 75, 100])
print("Minimum value of the series:")
print(series2[0])
print("\n25th percentile value of the numeric series:")
print(series2[1])
print("\nMedian value of the numeric series:")
print(series2[2])
print("\n75th percentile value of the numeric series:")
print(series2[3])
print("\nMaximum value of the the numeric series:")
print(series2[4])

"""
np.random.RandomState(100)

	RandomState exposes a number of methods for generating random numbers drawn from a variety of probability distributions. In addition to the distribution-specific arguments, each method takes a keyword argument size that defaults to None.
	If size is None, then a single value is generated and returned.
	
	
	If size is an integer, then a 1-D array filled with generated values is returned. If size is a tuple, then an array with that shape is filled and returned.
"""

"""
numpy.random.normal()

	Draw random samples from a normal (Gaussian) distribution.
"""

"""
numpy.percentile() in python
	
	numpy.percentile()function used to compute the nth precentile of the given data (array elements) along the specified axis.
"""	
