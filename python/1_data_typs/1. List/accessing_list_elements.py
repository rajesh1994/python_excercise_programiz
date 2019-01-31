l1 = ["Apple", "Banana", "Cricket", "Dance", "Energy", "Football", "Google"]
l2 = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

# We can use the index operator [] to access an item in a list. Index starts from 0. So, a list having 5 elements will have index from 0 to 4.
# Trying to access an element other that this will raise an IndexError. The index must be an integer. We can't use float or other types, this will result into TypeError.
# Nested list are accessed using nested indexing.

print "-" * 145
print "The list l1 is: ", l1

print "-" * 145
print "Element at index 5 in list l1 is: ", l1[5]

print "-" * 145
print "Element at index 2 in list l1 is: ", l1[2]

print "-" * 145
print "Element at index 0 in list l1 is: ", l1[0]

print "-" * 145
print "The list l2 is: ", l2

print "-" * 145
print "Element at index [5][0] in list l2 is: ", l2[5][0]
print "-" * 145
