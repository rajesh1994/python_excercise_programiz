"""
Problem Statement : 2. How to create a series from a list, numpy array and dict?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize list, numpy array & dict
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarray = np.arange(26)
mydict = dict(zip(mylist, myarray))

# Creating a series from a list, numpy array & dict
series1 = pd.Series(mylist)
series2 = pd.Series(myarray)
series3 = pd.Series(mydict)
print(series3.head(n = 10))

"""
Pandas head() method is used to return top n (5 by default) rows of a data frame or series.
"""
