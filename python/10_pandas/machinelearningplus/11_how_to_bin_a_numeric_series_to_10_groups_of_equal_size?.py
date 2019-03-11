"""
Problem Statement : 11. How to bin a numeric series to 10 groups of equal size?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1
series1 = pd.Series(np.random.random(20))
#print(series1)
print("Series with top 5 values:")
print(series1.head())

# Bin the series ser into 10 equal deciles and replace the values with the bin name
print(pd.qcut(series1, q = [0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1], labels = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']))

"""
pd.qcut()

	Quantile-based discretization function. Discretize variable into equal-sized buckets based on rank or based on sample quantiles. For example 1000 values for 10 quantiles would produce a Categorical object indicating quantile membership for each data point.
"""
