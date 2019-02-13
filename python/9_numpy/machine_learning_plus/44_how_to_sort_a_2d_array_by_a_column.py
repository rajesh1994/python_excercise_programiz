"""
Problem Statement : How to sort a 2D array by a column
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'float')

# Sort the iris dataset based on sepallength column.
# Sort by column sepallength(column 0)
print("Sort the iris dataset based on sepallength column:")
print(iris[iris[:,0].argsort()][:20])
