"""
Problem Statement : How to compute the mean, median, standard deviation of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Find the mean, median, standard deviation of iris's sepallength (1st column)

sepallength = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [1])
print("Sepal_Length column data:")
print(sepallength)

# Column sepallength's mean value
mean = np.mean(sepallength)
print("\nColumn sepallength's mean value:")
print(mean)

# Column sepallength's median value
median = np.median(sepallength)
print("\nColumn sepallength's median value:")
print(median)

# Column sepallength's standard deviation value
std = np.std(sepallength)
print("\nColumn sepallength's standard deviation value:")
print(std)

# Column sepallength's correlation coefficient value
corrcoef = np.corrcoef(sepallength)
print("\nColumn sepallength's correlation coefficient value:")
print(corrcoef)
