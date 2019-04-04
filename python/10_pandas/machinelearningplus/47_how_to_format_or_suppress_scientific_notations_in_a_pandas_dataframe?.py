"""
Problem Statement : 47. How to format or suppress scientific notations in a pandas dataframe?
"""
# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.

# Initializing DataFrame df1
df1 = pd.DataFrame(np.random.random(8) ** 10, columns = ['random'])
print("df1:")
print(df1)

# Solution 1 : Rounding
print("\nSolution 1: Rounding")
print(df1.round(4))

# Solution 2 : Using apply() to change format
print("\nSolution 2 : Using apply() to change format")
print(df1.apply(lambda x : '%.4f' %x, axis = 1))

# Solution 3 : Using applymap() to change format
print("\nSolution 3 : Using applymap() to change format")
print(df1.applymap(lambda x : '%.4f' %x))

# Solution 4 : Using set_option
print("\nSolution 4 : Using set_option")
pd.set_option('display.float_format', lambda x : '%.4f' %x)
print(df1)

# Solution 5 : Assign display.float_format
pd.options.display.float_format = '{:.4f}'.format
print("\nSolution 5 : Assign display.float_format")
print(df1)

# Reset/Undo float formatting
pd.options.display.float_format = None
print(df1)
