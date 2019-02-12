"""
Problem Statement : How to find the position of missing values in numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Find the number and position of missing values in iris_2d's sepallength (1st column)
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float')
iris_2d[np.random.randint(150, size = 20), np.random.randint(4, size = 20)] = np.nan

print("Number of missing values:\n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values:\n", np.where(np.isnan(iris_2d[:, 0])))
