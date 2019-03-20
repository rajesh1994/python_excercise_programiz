"""
Problem Statement : 25. How to filter valid emails from a series?
"""
# Import pandas as pd
# Import re
import pandas as pd
import re

series1 = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
print("series1:")
print(series1)

pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# Method 1: filter valid emails from a series(as a series of string)
mask = series1.map(lambda x : bool(re.match(pattern, x)))
print("\nMethod 1: filter valid emails from a series:")
print(series1[mask])

# Method 2: filter valid emails from a series(as a series of list)
print("\nMethod 2: filter valid emails from a series:")
print(series1.str.findall(pattern, flags = re.IGNORECASE))
