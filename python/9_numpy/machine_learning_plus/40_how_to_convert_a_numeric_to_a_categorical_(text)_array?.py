"""
Problem Statement : How to convert a numeric to a categorical (text) array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

"""
Bin the petal length (3rd) column of iris_2d to form a text array, such that if petal length is:

1. Less than 3 --> 'small'
2. 3-5 --> 'medium'
3. >=5 --> 'large'
"""

# Bin petallength
petal_length_bin = np.digitize(iris[:, 2].astype('float'), [0, 3, 5, 10])
