"""
Problem Statement : How to drop rows that contain a missing value from a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])
iris_2d[np.random.randint(150, size = 20), np.random.randint(4, size = 20)] = np.nan

# Select the rows of iris_2d that does not have any nan value.
# Method 1
print("Drop rows that contain a missing value from a numpy array:")
print("Method 1:")
any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[any_nan_in_row][:5])

# Method 2
print("\nMethod 2:")
print(iris_2d[np.sum(np.isnan(iris_2d), axis = 1) == 0][:5])
