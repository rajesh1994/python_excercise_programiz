"""
Problem Statement : 1.2 Length & Shape of Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initializing DataFrame
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Printing the shape of the DataFrame
print("Shape of the DataFrame:")
print(df.shape)

# Printing the length of the DataFrame
print("\nLength of the DataFrame:")
print(len(df.index))
