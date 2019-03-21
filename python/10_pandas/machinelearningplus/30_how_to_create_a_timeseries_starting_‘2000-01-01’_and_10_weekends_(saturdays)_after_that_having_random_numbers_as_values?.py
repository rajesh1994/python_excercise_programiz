"""
Problem Statement : 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) after that having random numbers as values?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initialize series1
series1 = pd.Series(np.random.randint(1, 10, 10), pd.date_range('2000-01-01', periods = 10, freq = 'W-SAT'))
print("TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) & random numbers as values:")
print(series1)

"""
pandas.date_range()

	pandas.date_range() is one of the general functions in Pandas which is used to return a fixed frequency DatetimeIndex.
	
Syntax:

	pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)

Parameters:

	start : Left bound for generating dates.
	end : Right bound for generating dates.
	periods : Number of periods to generate.
	freq : Frequency strings can have multiples, e.g. ‘5H’. See here for a list of frequency aliases.
	tz : Time zone name for returning localized DatetimeIndex. By default, the resulting DatetimeIndex is timezone-naive.
	normalize : Normalize start/end dates to midnight before generating date range.
	name : Name of the resulting DatetimeIndex.
	closed : Make the interval closed with respect to the given frequency to the ‘left’, ‘right’, or both sides (None, the default).

Returns:

	DatetimeIndex
