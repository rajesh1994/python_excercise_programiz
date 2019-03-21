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
