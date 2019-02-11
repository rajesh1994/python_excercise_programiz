"""
Problem Statement : How to normalize an array so the values range exactly between 0 and 1?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0])
print("Column sepallength:")
print(sepallength)
max1 = sepallength.max()
min1 = sepallength.min()
zero_one = (sepallength - min1)/(max1 - min1)
print("Values range exactly between 0 and 1:")
print(zero_one)
