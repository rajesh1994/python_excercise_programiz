# Arithmetic operations on numpy

# Import numpy as 'np'
import numpy as np

# Initialize 'x' & 'y'
x = np.arange(9.0).reshape(3, 3)
y = np.arange(3.0)
print("Array 'x' is:")
print(x)
print("\nArray 'y' is:")
print(y)

# Adding two arrays using np.add() method
add = np.add(x, y)
print("\nAddition of two arrays:")
print(add)

# Subtracting two arrays using np.subtract() method
sub = np.subtract(x, y)
print("\nSubtraction of two arrays:")
print(sub)

# Multiplying two arrays using np.multiply() method
mul = np.multiply(x, y)
print("\nMultiplication of two arrays:")
print(mul)

# Dividing two arrays using np.divide() method
div = np.divide(x, y)
print("\nDivision of two arrays:")
print(div)
