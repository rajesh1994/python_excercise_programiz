# Numpy's aggregate funtions:

# Import numpy as 'np'
import numpy as np

# Initialize 'x'
x = np.arange(9).reshape(3, 3)
print("Array 'x' is:")
print(x)

# Initialize 'y'
y = np.arange(9).reshape(3, 3)
print("\nArray 'y' is:")
print(y)

# Finding sum of elements using sum() method
sum1 = x.sum()
print("\nSum of the elements:")
print(sum1)

# Finding lowest element from the array using min() method
min1 = x.min()
print("\nLowest element from the array:")
print(min1)

# Finding highest element from the array using min() method
max1 = x.max()
print("\nHighest element from the array:")
print(max1)

# Finding mean value of the array using mean() method
mean = x.mean()
print("\nMean value of the array:")
print(mean)

# Finding median value of the array using meadian() method
median = np.median(x)
print("\nMedian value of the array:")
print(median)

# Finding correlation coefficient value of the array using corrcoef() method
corrcoef = np.corrcoef(x, y)
print("\nCorrelation coefficient value of the array:")
print(corrcoef)

# Finding standard deviation of the array using np.std() method
std_dev = np.std(x)
print("\nStandard deviation of the array:")
print(std_dev)

# Finding maximum value of an array in a row using max(axis = 0)
max2 = x.max(axis = 0)
print("\nMaximum value of an array in a row:")
print(max2)

# Finding minimum value of an array in a row using max(axis = 0)
max2 = x.min(axis = 0)
print("\nMinimum value of an array in a row:")
print(max2)

# Finding cumulative sum of the elements in a array using cumsum(axis = 0)
cumsum = x.cumsum()
print("Cumulative sum of the elements:")
print(cumsum)
print(cumsum)
