"""
Problem Statement : 28. How to find all the local maxima (or peaks) in a numeric series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Intialize series1
series1 = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
print("series1:")
print(series1)

# Find all the local maxima (or peaks) in a numeric series
dd = np.diff(np.sign(np.diff(series1)))
peak_locks = np.where(dd == -2)[0] + 1
print("\nPositions of peaks (values surrounded by smaller values on both sides) in series1:")
print(peak_locks)
