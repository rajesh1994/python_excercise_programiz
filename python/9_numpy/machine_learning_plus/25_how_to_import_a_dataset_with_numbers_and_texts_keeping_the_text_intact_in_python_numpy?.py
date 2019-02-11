"""
Problem Statement : How to import a dataset with numbers and texts keeping the text intact in python numpy?
"""

# Import numpy as 'np'
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# Printing first 3 rows
print("Printing first 3 rows:")
print(iris[: 3])
