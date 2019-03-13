"""
Problem Statement : 20. How to compute difference of differences between consequtive numbers of a series?
"""

# Import pandas as pd
import pandas as pd

# Initialize series1
series1 = pd.Series([1, 4, 5, 3, 8, 1, 10, 12, 22, 26])

print("Compute difference of differences between consequtive numbers of a series:")
print(series1.diff().tolist())
print(series1.diff().diff().tolist())
