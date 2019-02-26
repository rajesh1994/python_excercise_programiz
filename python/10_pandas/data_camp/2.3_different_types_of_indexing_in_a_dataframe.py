"""
Problem Statement : 2.3 Different types of indexing in a pandas dataframe
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index = [2, 'A', 4], columns = [48, 49, 50])
print("DataFrame 'df' is:")
print(df)


