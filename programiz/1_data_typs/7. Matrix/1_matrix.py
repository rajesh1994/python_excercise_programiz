"""
What is a matrix?

    A matrix is a two-dimensional data structure. In real-world tasks you often have to store rectangular data table.
    Such tables are called matrices or two-dimensional arrays.
    In python any table can be represented as a list of lists (a list, where each element is in turn a list).
    For example:

        A = [['Roy',80,75,85,90,95],['John',75,80,75,85,100],['Dave',80,80,80,90,95]]

        In the above example A represents a 3*6 matrix where 3 is number of rows and 6 is number of columns.
"""
"""
How to create a matrix?

    In python, matrix is a nested list.
    A list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.
"""

# Create a matrix in python

# m1 is 2-D matrix with integers
m1 = [['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95]]

# m2 is a nested list but not a matrix
nl1 = [['Roy', 80, 75, 85, 90, 95],
    ['John', 75, 80, 75],
    ['Dave', 80, 80, 80, 90, 95]]

print "*" * 140
print " " * 50, "1. Create a matrix in python"
print "Matrix m1 = ", m1
print "Nested list nl1 = ", nl1
print "*" * 140
