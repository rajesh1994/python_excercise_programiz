# Create a dynamic matrix using for loop in python

"""
    A possible way: you can create a matrix of n*m elements by first creating a list of n elements (say, of n zeros) and then make each of the elements a link to another one-dimensional list of m elements:
"""

n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print "a = ", a
