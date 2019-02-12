"""
Problem Statement : How to create a new column from existing columns of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'object')
print("Original array:")
print(iris_2d[:10])

# Create a new column for volume in iris_2d, where volume is (pi x petallength x sepal_length^2)/3
# Computing the voulume
sepallength = iris_2d[:, 0].astype('float')
petallength = iris_2d[:, 2].astype('float')
volume = (np.pi * petallength * (sepallength ** 2)) // 3

# Introduce new dimension to match iris_2d's
volume = volume[:, np.newaxis]

# Add new column
# New column from existing columns of a array
out = np.hstack([iris_2d, volume])
print("\nNew column from existing columns of a array:")
print(out[:10])
