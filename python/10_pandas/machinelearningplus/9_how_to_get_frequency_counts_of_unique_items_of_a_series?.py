"""
Problem Statement : 9. How to get frequency counts of unique items of a series?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Initilize series1
series1 = pd.Series(np.take(list("abcdefghi"), np.random.randint(8, size = 30)))
print("Series1:")
print(series1)
# Calculating the frequency value of unique items of a series
print("\nCalculating the frequency value of unique items of a series:")
print(series1.value_counts())
