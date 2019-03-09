"""
Problem Statement : 6. How to get the items of series A not present in series B?
"""

# Import pandas as pd
import pandas as pd

# Initialize series1 & series2
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

# Printing series1 & series2
print("Series1:")
print(series1)
print("\nSeries2:")
print(series2)

# Getting the items of series 1 not present in series 2
print("\nGetting the items of series 1 not present in series 2:")
print(series1[~series1.isin(series2)])

"""
isin() method:

Pandas isin() method is used to filter data frames. isin() method helps in selecting rows with having a particular(or Multiple) value in a particular column.

Syntax:
DataFrame.isin(values)

Parameters:
values: iterable, Series, List, Tuple, DataFrame or dictionary to check in the caller Series/Data Frame.

Return Type: 
DataFrame of Boolean of Dimension.
"""
