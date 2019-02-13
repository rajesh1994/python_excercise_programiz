"""
Problem Statement : How to find the correlation between two columns of a numpy array?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

# Find the correlation between SepalLength(1st column) and PetalLength(3rd column) in iris_2d
corrcoef = np.corrcoef(iris_2d[:, 0], iris_2d[:, 2])[0, 1]
print("correlation between SepalLength(1st column) and column(PetalLength 3rd) in iris_2d:")
print(corrcoef)

"""
Correlation Coefficient:
1. Correlation coef indicates the degree of linear relationship between two numeric variables.
2. It can range between -1 to +1.
3. The p-value roughly indicates the probability of an uncorrelated system producing 
4. datasets that have a correlation at least as extreme as the one computed.
5. The lower the p-value (<0.01), stronger is the significance of the relationship.
6. It is not an indicator of the strength.
"""
