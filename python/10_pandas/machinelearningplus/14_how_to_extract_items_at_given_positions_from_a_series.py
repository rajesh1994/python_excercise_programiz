"""
Problem Statement : 14. How to extract items at given positions from a series
"""

# Import pandas as pd
import pandas as pd

# Initialize series1
series1 = pd.Series(list("abcdefghijklmnopqrstuvwxyz"))
position = [0, 8, 12, 18, 17, 26]

# Extracting items at 0, 8, 12, 18, 17, 26 positions from a series
print("Extracting items at 0, 8, 12, 18, 17, 26 positions from a series:")
print(series1.take(pos))
