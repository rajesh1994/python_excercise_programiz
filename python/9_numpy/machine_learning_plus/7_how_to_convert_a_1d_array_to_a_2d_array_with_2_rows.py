"""
Problem Statement : How to convert a 1D array to a 2D array with 2 rows
"""

# Import numpy as 'np'
import numpy as np

# Initializing a 1D array 'x'
x = np.arange(10)
print("1D array:")
print(x)

# Reshaping a 1D array to 2D array with 2 rows
y = x.reshape(2, -1) # Setting to -1 automatically decides the number of cols
print("\nReshaped 2D array:")
print(y)
