"""
Problem Statement : How to find the most frequent value in a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype ='object')

# Find the most frequent value of petal length (3rd column) in iris dataset
vals, counts = np.unique(iris[:, 2])
