"""
Problem Statement : How to get the second largest value of an array when grouped by another array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# What is the value of second longest petallength of species setosa

# Get the species & petal length column
petal_len_setosa = iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float')
print("Species & petal length column:")
print(np.sort(petal_len_setosa))
# Get the second last value
print("\nSecond last value of species setosa:")
print(np.unique(np.sort(petal_len_setosa))[-2])
