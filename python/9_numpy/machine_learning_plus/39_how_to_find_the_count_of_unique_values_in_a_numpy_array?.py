"""
Problem Statement : How to find the count of unique values in a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# Find the unique values and the count of unique values in iris's species
species = np.array([row.tolist()[4] for row in iris])
unique = np.unique(species, return_counts = True)
print("Unique values and the count of unique values in iris's species:")
print(unique)
