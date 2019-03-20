"""
Problem Statement : 22. How to get the day of month, week number, day of year and day of week from a series of date strings?
"""

# Import pandas as pd
# Import parse from dateutil.parser
import pandas as pd
from dateutil.parser import parse

# Initialize series1
series1 = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
print("series1:")
print(series1)

# get the day of month, week number, day of year and day of week from a series of date strings
series2 = series1.map(lambda x : parse(x))

# Day of the month
print("\nDay of the month:", series2.dt.day.tolist())

# Week number
print("\nWeek number:", series2.dt.weekofyear.tolist())

# Day of year
print("\nDay of year:", series2.dt.dayofyear.tolist())

# Day of week
print("\nDay of week:", series2.dt.weekday_name.tolist())
