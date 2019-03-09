"""
Problem Statement : 7. How to get the items not common to both series A and series B?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initialize series1 & series2
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

# Printing series1 & series2
print("Series1:")
print(series1)
print("\nSeries2:")
print(series2)

# Getting the items not common to both series 1 & series 2
series_union = pd.Series(np.union1d(series1, series2))
print("\nUnion of two series are:")
print(series_union)

series_intersect = pd.Series(np.intersect1d(series1, series2))
print("\nIntersect of two series are:")
print(series_intersect)

print("\nGetting the items not common to both series 1 & series 2:")
print(series_union[~series_union.isin(series_intersect)])
