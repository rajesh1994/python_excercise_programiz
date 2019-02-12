"""
Problem Statement : How to find the percentile scores of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0])

# Getting percentile scores of a column sepallength
percentile_score = np.percentile(sepallength, q = [5, 95])
print("Percentile scores of a column sepallength:")
print(percentile_score)
