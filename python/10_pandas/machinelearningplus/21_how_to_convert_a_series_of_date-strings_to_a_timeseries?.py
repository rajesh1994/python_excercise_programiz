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

"""
pd.to_datetime()

Pandas to_datetime() method helps to convert string Date time into Python Date time object.

 Syntax:

pandas.to_datetime(arg, errors=’raise’, dayfirst=False, yearfirst=False, utc=None, box=True, format=None, exact=True, unit=None, infer_datetime_format=False, origin=’unix’, cache=False)

 
Parameters:

arg: An integer, string, float, list or dict object to convert in to Date time object.
dayfirst: Boolean value, places day first if True.
yearfirst: Boolean value, places year first if True.
utc: Boolean value, Returns time in UTC if True.
format: String input to tell position of day, month and year.

Return type: Date time object series.
"""
