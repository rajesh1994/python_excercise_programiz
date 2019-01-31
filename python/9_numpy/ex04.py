# How To Save NumPy Arrays

import numpy as np

x = np.arange(0, 10, 1)
np.savetxt('test.txt', x, delimiter = ',')
