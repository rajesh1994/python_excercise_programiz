# How To Visualize NumPy Arrays

# Import numpy as 'np'
import numpy as np

# Initialize array 'x'
x = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[9,10,11,12]]], dtype = np.int64)

# Pass the array to np.histogram() method
print(np.histogram(x))

# Specify the number of bins
print(np.histogram(x, bins = range(0, 13)))
