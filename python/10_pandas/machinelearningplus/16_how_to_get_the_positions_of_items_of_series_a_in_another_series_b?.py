"""
Problem Statement : 16. How to get the positions of items of series A in another series B?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1 & series2
series1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
series2 = pd.Series([1, 3, 10, 13])
print("Series1:")
print(series1)
print("\nSeries2:")
print(series2)

# Method 1 : Getting the postions of items of series1 in another series2
print("\nMethod 1 : Getting the postions of items of series1 in another series2:")
print([np.where(i == series1)[0].tolist()[0] for i in series2])

# Method 2 : Getting the postions of items of series1 in another series2
print("\nMethod 2 : Getting the postions of items of series1 in another series2:")
print([pd.Index(series1).get_loc(i) for i in series2])
