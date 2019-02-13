"""
Problem Statement : How to do probabilistic sampling in numpy?
"""

# Import numpy as 'np'
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')

# Randomly sample iris's species such that setose is twice the number of versicolor and virginica
# Get the species column
species = iris[:,4]

# Approach 1: Generate Probablistically
np.random.seed(100)
a = np.array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
species_out = np.random.choice(a, 150, p = [0.5, 0.25, 0.25])
print("Probabilistic sampling:")
print(species_out)

# Approach 2: Probablistic Sampling (preferred)
np.random.seed(100)
probs = np.r_[np.linespace(0, 0.500, num = 50), np.linespace(0.501, 0.750, num = 50), np.linespace(0.751, 1, num = 50)]
index = np.searchsorted(probs, np.random.random(150))
species_out = species[index]
print(np.unique(species_out, return_counts = True))
