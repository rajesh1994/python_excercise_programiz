l1 = [1, 2, "Three", "Four"]
l2 = [5, 6, "Seven", "Eight"]

# We can also use + operator to combine two lists. This is also called concatenation.
list_add = l1 + l2

print "*" * 145
print "List l1 is: ", l1

print "*" * 145
print "List l2 is: ", l2

print "*" * 145
print "Concatenated list: ", list_add

# The * operator repeats a list for the given number of times
l3 = ["Apple", "Banana", "Cat", "Dove"]

multiply_list = l3 * 3

print "*" * 145
print "Multiplied list: ", multiply_list

#We can delete one or more items from a list using the keyword del. It can even delete the list entirely.
l4 = ['P', 'y', 't', 'h', 'o', 'n']
l5 = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

print "*" * 145

print "Actual values in list l4: ", l4
del l4[5]

print "After deleting data in index 5 in list l4: ", l4

print "*" * 145
print "Actual values in list l5: ", l5

del l5[4 : 8]

print "After deleting data from index 4 to 8: ", l5
print "*" * 145

# Delete entire list
l6 = ["Apple"]

"""
print "*" * 145
print "Actual list l6: ", l6

del l6

print "After deleting list l6: ", l6
"""
