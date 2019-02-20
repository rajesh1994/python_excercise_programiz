"""
Problem Statement : How to find the grouped mean in numpy?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')


# Find the mean of a numeric column grouped by a categorical column in a 2D numpy array
# Solution
# No direct way to implement this. Just a version of a workaround.
numeric_column = iris[:, 1].astype('float') # Sepalwidth
grouping_column = iris[:, 4] # Species

# For loop version
output1 = []
for group_val in np.unique(grouping_column):
    output1.append([group_val, numeric_column[grouping_column == group_val].mean()])
print("For loop version\nGrouped mean of column species:")
print(output1)

# List comprehension version
output2 = [[group_val, numeric_column[grouping_column == group_val].mean()] for group_val in np.unique(grouping_column)]
print("\nList comprehension version:\nGrouped mean of column species:")
print(output2)
