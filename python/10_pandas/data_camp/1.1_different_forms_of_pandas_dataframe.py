"""
Problem Statement : 1.1 Different Forms of Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Take 2d array as input to your DataFrame
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])

# Printing my_2darray array as a form of DataFrame
print(pd.DataFrame(data = my_2darray[0:, 0:]))
