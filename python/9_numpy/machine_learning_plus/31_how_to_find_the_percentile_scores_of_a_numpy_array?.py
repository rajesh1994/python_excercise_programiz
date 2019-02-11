"""
Problem Statement : How to find the percentile scores of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtext(url, delimiter = ',', dtype = 'float', usecols = [0])
