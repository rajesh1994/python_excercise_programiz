"""
Problem Statement : How to replace all missing values with 0 in a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

# Replace all occurrences of nan with 0 in numpy array
iris_2d[np.isnan(iris_2d)] = 0
print("Replace all occurrences of nan with 0 in array iris_2d:")
print(iris_2d[:4])
