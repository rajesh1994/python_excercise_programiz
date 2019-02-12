"""
Problem Statement : How to find if a given array has any null values?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

# Find out if iris_2d has any missing values
null = np.isnan(iris_2d).any()
print(null)
