"""
Problem Statement : How to do probabilistic sampling in numpy?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# Randomly sample iris's species such that setose is twice the number of versicolor and virginica

