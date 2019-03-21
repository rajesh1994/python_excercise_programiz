"""
Problem Statement : 31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initialize series1
series1 = pd.Series([1, 10, 22, np.nan], index = pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))

# Solution
print(series1.resample('D').ffill())

"""
series.ffill()

	Pandas dataframe.ffill() function is used to fill the missing value in the dataframe. ‘ffill’ stands for ‘forward fill’ and will propagate last valid observation forward.

Syntax:

series.ffill(axis=None, inplace=False, limit=None, downcast=None)

Parameters:
    axis : {0, index 1, column}
    inplace : If True, fill in place. Note: this will modify any other views on this object, (e.g. a no-copy slice for a column in a DataFrame).
    limit : If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None.
    Downcast: a dict of item->dtype of what to downcast if possible, or the string ‘infer’ which will try to downcast to an appropriate equal type (e.g. float64 to int64 if possible)
    
Returns : 
	filled : Series
"""

"""
series.bfill()

	Pandas dataframe.bfill() is used to backward fill the missing values in the dataset. It will backward fill the NaN values that are present in the pandas dataframe.

Syntax: DataFrame.bfill(axis=None, inplace=False, limit=None, downcast=None)

Parameters:
    axis : ‘rows’ or ‘columns’
    inplace : boolean, default False
    limit : integer value, No. of consecutive na cells to be populated.
"""

"""
series.resample()
	Pandas dataframe.resample() function is primarily used for time series data.
A time series is a series of data points indexed (or listed or graphed) in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time. It is a Convenience method for frequency conversion and resampling of time series. Object must have a datetime-like index (DatetimeIndex, PeriodIndex, or TimedeltaIndex), or pass datetime-like values to the on or level keyword.

Syntax :
	DataFrame.resample(rule, how=None, axis=0, fill_method=None, closed=None, label=None, convention=’start’, kind=None, loffset=None, limit=None, base=0, on=None, level=None)

Parameters :
    rule : the offset string or object representing target conversion
    axis : int, optional, default 0
    closed : {‘right’, ‘left’}
    label : {‘right’, ‘left’}
    convention : For PeriodIndex only, controls whether to use the start or end of rule
    loffset : Adjust the resampled time labels
    base : For frequencies that evenly subdivide 1 day, the “origin” of the aggregated intervals. For example, for ‘5min’ frequency, base could range from 0 through 4. Defaults to 0.
    on : For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.
    level : For a MultiIndex, level (name or number) to use for resampling. Level must be datetime-like. 

	Resampling generates a unique sampling distribution on the basis of the actual data. We can apply various frequency to resample our time series data. This is a very important technique in the field of analytics.

Most commonly used time series frequency are –
W : weekly frequency
M : month end frequency
SM : semi-month end frequency (15th and end of month)
Q : quarter end frequency

URL :
https://www.geeksforgeeks.org/python-pandas-dataframe-resample/
"""
