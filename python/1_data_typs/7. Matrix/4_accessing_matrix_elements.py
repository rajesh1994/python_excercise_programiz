# How to access elements in a matrix?
"""
1. List Index

    Similar to list we can access elements of a matrix by using square brackets [] after the variable like a[row][col].
"""

# Accessing elements of the matrix in python by using list index

m1 = [['Roy', 80, 85, 75, 90, 95],
    ['John', 75, 80, 75, 85, 100],
    ['Dave', 80, 80, 80, 90, 95]]

print "*" * 145
print " " * 50, "1. Accessing elements of the matrix in python by using list index"
print "m1 = ", m1
print "m1[0] = ", m1[0]
print "m1[0][1] = ", m1[0][1]
print "m1[1][2] = ", m1[1][2]

# Negative Indexing
"""
    Python allows negative indexing for its sequences.
    The index of -1 refers to the last item, -2 to the second last item and so on.
"""
# Accessing elements of the matrix in python by using negative list index

print "*" * 145
print " " * 50, "2. Accessing elements of the matrix in python by using negative list index"
print "m1 = ", m1
print "m1[-1] = ", m1[-1]
print "m1[-1][-2] = ", m1[-1][-2]
print "m1[-2][-3] = ", m1[-1][-2]
print "*" * 145
