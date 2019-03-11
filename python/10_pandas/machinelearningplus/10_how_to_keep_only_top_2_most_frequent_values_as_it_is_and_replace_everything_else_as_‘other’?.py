"""
Problem Statement : 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1
np.random.RandomState(100)
series1 = pd.Series(np.random.randint(1, 5, [12]))
#print(series1)

# Keep only top 2 most frequent values
print("Keep only top 2 most frequent values:", series1.value_counts())
series1[~series1.isin(series1.value_counts().index[:2])] = "Other"
print(series1)
