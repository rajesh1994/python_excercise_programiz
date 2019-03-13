"""
Problem Statement : 15. How to stack two series vertically and horizontally ?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1 & series2
series1 = pd.Series(np.arange(5))
series2 = pd.Series(list("abcde"))

# Stack two series vertically
print("Stack two series vertically:")
print(series1.append(series2))

# Stack two series horizontally
print("Stack two series horizontally:")
print(pd.concat([series1, series2], axis = 1))
