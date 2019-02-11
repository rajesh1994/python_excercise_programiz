"""
Problem Statement : How to extract a particular column from 1D array of tuples?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_id = np.genfromtxt(url, delimiter = ',', dtype = None)
print("Shape of the array:")
print(iris_id.shape)

column = np.array([row[4] for row in iris_id])
print(column[:5])
