"""
Problem Statement : How to convert a 1d array of tuples to a 2d numpy array?
"""

# Import  numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter = ',', dtype = None)
print("1D array is:")
print(iris_1d)

# Method 1: Convert each row to a list & get first 4 items
iris_2d_m1 = np.array([row.tolist()[:4] for row in iris_1d])
print("Convert each row to a list & get first 4 items:")
print(iris_2d_m1[:4])

# Method 2: Import first 4 rows from source url
iris_2d_m2 = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])
print("Import first 4 rows from source url:")
print(iris_2d_m2[:4])
