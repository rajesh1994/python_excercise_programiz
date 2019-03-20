"""
Problem Statement : 26. How to get the mean of a series grouped by another series?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Intialize fruits & weight
fruits = pd.Series(np.random.choice(['Apple', 'Banana', 'Carrot', 'Lime'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print('fruits:')
print(fruits)
print('weights:')
print(weights)

# Mean of weights of each fruit
print("Mean of weights of each fruit:")
print(weights.groupby(fruits).mean())
