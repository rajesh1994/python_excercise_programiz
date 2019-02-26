"""
Problem Statement : 1. How To Create a Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initializing an array 'data'
data = np.array([['', 'Col1', 'Col2'], ['Row1', 1, 2], ['Row2', 3, 4]])

# printing a DataFrame
print("Pandas DataFrame:")
print(pd.DataFrame(data = data[1:, 1:], index = data[1:, 0], columns = data[0, 1:]))
