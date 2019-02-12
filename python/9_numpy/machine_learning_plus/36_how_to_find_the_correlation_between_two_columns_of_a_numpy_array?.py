"""
Problem Statement : How to find the correlation between two columns of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

# Find the correlation between SepalLength(1st column) and PetalLength(3rd column) in iris_2d
corrcoef = np.corrcoef(iris_2d[:, 0], iris_2d[:, 2])[0, 1]
print("correlation between SepalLength(1st column) and column(PetalLength 3rd) in iris_2d:")
print(corrcoef)
