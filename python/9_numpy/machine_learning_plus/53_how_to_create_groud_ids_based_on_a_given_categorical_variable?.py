"""
Problem Statement : How to create groud ids based on a given categorical variable?
"""

# Import numpy as 'np'
import numpy as np

# Create group ids based on a given categorical variable. Use the following sample from iris species as input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
species = np.genfromtxt(url, delimiter = ',', dtype = 'str', usecols = 4)
np.random.seed(100)
species_small = np.sort(np.random.choice(species, size = 20))
print("Species small array:")
print(species_small)

# Solution : Using For loop
output = []
uniqs = np.unique(species_small)
for val in uniqs:
    for s in species_small[species_small == val]: # Each element in group
        groupid = np.argwhere(uniqs == s).tolist()[0][0] # groupid
        output.append(groupid)
print("\nGroup ids based on a given categorical variable:")
print(output)
