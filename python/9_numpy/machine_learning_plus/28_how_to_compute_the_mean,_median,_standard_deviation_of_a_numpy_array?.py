"""
Problem Statement : How to compute the mean, median, standard deviation of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = None)

# Find the mean, median, standard deviation of iris's sepallength (1st column)

sepallength = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [1])
print("Sepal_Length column data:")
print(sepallength)

# Mean value of the column sepallength
mean = np.mean(sepallength)
print("\nMean value of the column sepallength:")
print(mean)

# Median value of the column sepallength
median = np.median(sepallength)
print("\nMedian value of the column sepallength:")
print(median)
