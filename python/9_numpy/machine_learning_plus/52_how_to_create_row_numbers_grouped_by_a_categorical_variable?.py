"""
Problem Statement : How to create row numbers grouped by a categorical variable?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Create row numbers grouped by a categorical variable. Use the following sample from iris species as input.
species = np.genfromtxt(url, delimiter = ',', dtype = 'str', usecols = [4])
species_small = np.sort(np.random.choice(species, size = 20))
print("Array 'Species Small':")
print(species_small)

# Create row numbers grouped by a categorical variable. Use the following sample from iris species as input.
print([i for val in np.unique(species_small) for i, grp in enumerate(species_small[species_small == val])])
