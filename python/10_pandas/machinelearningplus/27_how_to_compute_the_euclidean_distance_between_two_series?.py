"""
Problem Statement : 27. How to compute the euclidean distance between two series?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initialize series1 & series2
series1 = pd.Series([i for i in range(10)])
series2 = pd.Series([i for i in range(9, -1, -1)])

"""
print('series1:')
print(series1)
print('\nseries2:')
print(series2)
"""

# Method 1: compute the euclidean distance between two series
print("\nMethod 1: Euclidean distance between two series")
print(round(sum((series1 - series2)**2)**.5, 2))

# Method 2: Euclidean distance between two series
print("\nMethod 2: Euclidean distance between two series")
print(round(np.linalg.norm(series1 - series2), 2))
