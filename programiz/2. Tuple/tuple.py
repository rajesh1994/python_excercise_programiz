"""
What is tuple?

    In Python programming, a tuple is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list, elements can be changed.

Creating a Tuple:

    A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma. The parentheses are optional but is a good practice to write it.

    A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).
    
"""
print "*" * 145
t1 = ()
print "This is empty tuple: ", t1

print "*" * 145
t2 = (1, 2, 3, 4, 5)
print "Tuple with five elements: ", t2

print "*" * 145
t3 = (1, 2, 3, 4, (5, 6, 7, 8))
print "Nested tuple: ", t3

print "*" * 145
# Creating tuple with one element
"""
Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.
"""
t4 = ("Hello")

print "Tuple t4 have only one element: ", t4

print "*" * 145
t5 = 9, 10, 11, 12, 13
print "Parentheses is optional for tuples: ", t5
print "*" * 145
