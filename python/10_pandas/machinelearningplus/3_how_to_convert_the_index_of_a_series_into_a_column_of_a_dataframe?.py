"""
Problem Statement : 3. How to convert the index of a series into a column of a dataframe?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarray = np.arange(26)
mydict = dict(zip(mylist, myarray))
series = pd.Series(mydict)
print("Series:")
print(series.head())

# Converting the index of a series into a column of a DataFrame
print("\nConverting the index of a series into a column of a DataFrame:")
print(series.to_frame().reset_index().head())

"""
to_frame() method:

The to_frame() method is used to convert the Series into DataFrame
"""

"""
reset_index():

Pandas reset_index() is a method to reset index of a Data Frame. reset_index() method sets a list of integer ranging from 0 to length of data as index.

Syntax:
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”)

Parameters:
level: int, string or a list to select and remove passed column from index.

drop: Boolean value, Adds the replaced index column to the data if False.

inplace: Boolean value, make changes in the original data frame itself if True.

col_level: Select in which column level to insert the labels.

col_fill: Object, to determine how the other levels are named.

Return type: DataFrame
"""
