"""
Problem Statement : 21. How to convert a series of date-strings to a timeseries?
"""

# Import pandas as pd
# Import parse from dateutil
import pandas as pd
from dateutil.parser import parse

# Initilize Series1
series1 = pd.Series(['01 Jan 2010', '02-02-2002', '20100202', '04/12/2019', '2015-06-06T12:20'])
print("series1:")
print(series1)

# Method 1 : converting a series of date-strings to a timeseries
print("\nMethod 1 : converting a series of date-strings to a timeseries")
print(series1.map(lambda x : parse(x)))

# Method 2 : converting a series of date-strings to a timeseries
print("\nMethod 2 : converting a series of date-strings to a timeseries")
print(pd.to_datetime(series1))
