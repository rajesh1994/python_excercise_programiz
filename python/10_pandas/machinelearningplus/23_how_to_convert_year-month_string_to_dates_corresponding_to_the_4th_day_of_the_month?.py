"""
Problem Statement : 23. How to convert year-month string to dates corresponding to the 4th day of the month?
"""

# Import pandas as pd
# Import parse from dateutil.parser
import pandas as pd
from dateutil.parser import parse

# Intialize series1
series1 = pd.Series(['Jan 2019', 'Mar 1994', 'May 1998', 'Oct 2000', 'Dec 2015'])
print("Series1:")
print(series1)

# Method 1: convert year-month string to dates corresponding to the 4th day of the month
print("\nMethod 1: convert year-month string to dates corresponding to the 4th day of the month")
print(series1.map(lambda x : parse('04' + x)))

# Method 2: convert year-month string to dates corresponding to the 4th day of the month
# Parse the date
parse_date = series1.map(lambda x : parse(x))

# Construct date string with date as 4
series_datestr = parse_date.dt.year.astype('str') + '-' + parse_date.dt.month.astype('str') + '-' + '04'
print("\nMethod 2: convert year-month string to dates corresponding to the 4th day of the month")
print(series_datestr)
