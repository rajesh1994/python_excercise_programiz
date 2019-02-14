"""
Problem Statement : How to find the position of the first occurrence of a value greater than a given value?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])
#print(iris[:50])
# Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
print("First occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset:")
print(np.argwhere(iris[:, 3].astype(float) > 1.0)[0])
