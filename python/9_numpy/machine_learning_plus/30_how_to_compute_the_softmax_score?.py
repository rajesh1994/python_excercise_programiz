"""
Problem Statement : How to compute the softmax score?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0])

# Compute softmax values from each sets of scores in x
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis = 0)
print("Softmax score of the column sepallength:")
print(softmax(sepallength))
