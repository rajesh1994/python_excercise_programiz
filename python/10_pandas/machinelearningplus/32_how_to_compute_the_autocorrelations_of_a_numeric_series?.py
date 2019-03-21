"""
Problem Statement : 32. How to compute the autocorrelations of a numeric series?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize series1
series1 = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
print("series1:")
print(series1)

# compute the autocorrelations of a numeric series
auto_correlations = [series1.autocorr(i) for i in range(11)]
print("\nAutocorrelations of a numeric series:")
print(auto_correlations[1:])
print("\nLag having highest correlation:", np.argmax(np.abs(auto_correlations[1:])) + 1)
