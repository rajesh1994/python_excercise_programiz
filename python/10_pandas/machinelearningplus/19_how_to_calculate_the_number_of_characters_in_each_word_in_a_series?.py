"""
Problem Statement : 19. How to calculate the number of characters in each word in a series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1
series1 = pd.Series(["Love", "India", "Python", "Chemistry"])
print("Series1:")
print(series1)

# Number of characters in each word
print("\nNumber of characters in each word:")
print(series1.map(lambda x : len(x)))
