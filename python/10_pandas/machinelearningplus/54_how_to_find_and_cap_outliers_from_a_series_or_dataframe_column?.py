"""
Problem Statement : 54. How to find and cap outliers from a series or dataframe column?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize Series
series = pd.Series(np.logspace(-2, 2, 5, base=2))
#print(series)

# Solution
def cap_outliers(series, low, high):
    low, high = series.quantile([low, high])
    print(low, "%ile: ", low, "|", high, "%ile: ", high)
    series[series < low] = low
    series[series > high] = high
    return (series)
cap_outliers(series, .05, .95)