"""
Problem Statement : How to create groud ids based on a given categorical variable?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'float')

# What is the value of second longest petallength of species setosa
# Get the species & petal length column
petal_length_setosa = iris[iris[:, 4] == b'Iris-setosa', [2]]

# Get the second last value
print("Second longest petallength of species setosa:")
print(np.unique(np.sort(petal_length_setosa))[-2])
