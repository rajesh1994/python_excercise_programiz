"""
1. Indexing:

    We can use the index operator [] to access an item in a tuple where the index starts from 0.

    So, a tuple having 6 elements will have index from 0 to 5. Trying to access an element other that (6, 7,...) will raise an IndexError.

    The index must be an integer, so we cannot use float or other types. This will result into TypeError.

    Likewise, nested tuple are accessed using nested indexing, as shown in the example below.
"""

print "*" * 145
print " " * 65, "1. Indexing", " " * 68

t1 = 1, 2, 3, 4, 5, 6, 7, 8, 9

print "*" * 145
print "Actual tuple t1 is: ", t1

print "*" * 145
print "5th element in the tuple t1 is: ", t1[5]

print "*" * 145
print "10th element in the tuple t1 is: ", t1[8]

t2 = (10, 90, (20, 21, 99, 30, 40), 22, 32, 45)

print "*" * 145
print "Actual tuple t2 is: ", t2

print "*" * 145
print "Element at index [2][1] in the tuple t2 is: ", t2[2][1]
print "*" * 145

"""
2. Negative Indexing:

Python allows negative indexing for its sequences.

The index of -1 refers to the last item, -2 to the second last item and so on.
"""
print " " * 65, "2. Negative Indexing", " " * 68

t3 = 11, 12, 13, 14, 15, 23, 32, 19

print "*" * 145
print "Actual tuple t3 is: ", t3

print "*" * 145
print "Element at index -5 in the tuple t3 is: ", t3[-5]

print "*" * 145
print "Element at index -2 in the tuple t3 is: ", t3[-2]

print "*" * 145
print "Element at index -0 in the tuple t3 is: ", t3[-0]
print "*" * 145

"""
3. Slicing:

We can access a range of items in a tuple by using the slicing operator - colon ":".
"""

print " " * 65, "3. Slicing", " " * 68

t4 = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'

print "*" * 145
print "Actual tuple t4 is: ", t4

print "*" * 145
print "Slicing the elements between index 2 to 6 in tuple t4: ", t4[2:6]

print "*" * 145
print "Slicing the whole elements in the tuple t4: ", t4[:]

print "*" * 145
print "Slicing the elements from the beggining to 5th index: ", t4[: 5]

print "*" * 145
print "Slicing the elements from 2nd index to end of the tuple: ", t4[2:]
print "*" * 145
