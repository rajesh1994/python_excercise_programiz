# How To Load NumPy Arrays From Text

import numpy as np

x, y, z = np.loadtxt('data.txt', skiprows = 1, unpack = True)
print(x, y, z)
