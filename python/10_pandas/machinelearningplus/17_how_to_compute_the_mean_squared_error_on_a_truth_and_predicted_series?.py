"""
Problem Statement : 17. How to compute the mean squared error on a truth and predicted series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize truth & predicted
truth = pd.Series(np.arange(10))
predicted = pd.Series(np.arange(10) + np.random.random(10))
print("Series truth :")
print(truth)
print("\nSeries Predicted:")
print(predicted)

# Computing the mean squared error on a truth & predicted
print("\nComputing the mean squared error on a truth & predicted:")
print(np.mean((truth - predicted) ** 2))
