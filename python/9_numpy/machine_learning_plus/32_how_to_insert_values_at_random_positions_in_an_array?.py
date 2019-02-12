"""
Problem Statement : How to insert values at random positions in an array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# Method 1:
i, j = np.where(iris_2d)

# i, j contain row numbers & column numbers of 600 elements of iris_2d
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
print("Method 1:")
print(iris_2d[: 10])

# Method 2:
np.random.seed(100)
iris_2d[np.random.randint(150, size = 20), np.random.randint(4, size = 4)] = np.nan
print("\nMethod 2:")
print(iris_2d[: 10])
