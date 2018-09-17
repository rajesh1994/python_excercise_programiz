# The range() function

"""
    We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

    We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.

    This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.

    To force this function to output all the items, we can use the function list().
"""

print "*" * 143
print " " * 50, "1. Python range() function"
print range(10)

print tuple(range(10))

print list(range(2, 8))

print list(range(50, -50, -4))

print list(range(-50, 50, 4))
print "*" * 143
