"""
Problem Statement : How to filter a numpy array based on two or more conditions?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)

# Printing the values between 1.5 to 5.0 in petallength column & sepllength
print("Values between 1.5 to 5.0 in petallength column & sepllength:")
print(iris_2d[condition])
