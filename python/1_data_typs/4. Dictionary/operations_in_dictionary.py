"""
How to access elements from a dictionary?

    While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method.

    The difference while using get() is that it returns None instead of KeyError, if the key is not found.
"""

d1 = {"name" : "Jack Sparrow", "age" : 23}

print "*" * 145
print " " * 50, "1. Access elements from a Dictionary"

print "d1 = ", d1
print "Name = ", d1["name"]
print "Age = ", d1["age"]

d1["age"] = 24

"""
How to change or add elements in a dictionary?

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.

If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
"""

print "*" * 145
print " " * 50, "2. Change elements in a Dictionary"

print "After changing age in dictionary: d1 = ", d1


d1["Address"] = "Downtown"

print "*" * 145
print " " * 50, "3. Add elements in a dictionary"

print "After adding one key : value pair in dictionary: d1 = ", d1

"""
How to delete or remove elements from a dictionary?

    We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.

    The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.

    We can also use the del keyword to remove individual items or the entire dictionary itself.
"""

d2 = {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
d3 = {6 : 36, 7 : 49, 8 : 64, 9 : 81}
d4 = {10 : 100, 11 : 121}

print "*" * 145
print " " * 50, "4. Delete or remove elements from a dictionary"
print "d2 = ", d2
d2.pop(5)
print "After removing one value from dictionary: d2 = ", d2


print "*" * 145
print "d2 = ", d2
d2.popitem()
print "After removing one key : value pair from dictionary: d2 = ", d2


print "*" * 145
print "d3 = ", d3
d3.clear()
print "After clearing all key : value pair from dictionary: d3 = ", d3

print "*" * 145
print "d4 = ", d4
del d4[10]
print "deleting a particular item in a dictionary: d4 = ", d4

"""
del d4
print "*" * 145
print "deleting entire dictionary:", d4
"""

# The len() function returns the number of items (length) of an object.

d5 = {"Name" : "Jack", "Age" : 22, "Gender" : "M"}

print "*" * 145
print "Length of the dictionary d5 = ", len(d5)
print "*" * 145

# Compares items of two dictionaries.

#d6 = {1 : "Blue", 2 : "Yellow", 3 : "Green"}
d6 = {1 : "Black", 2 : "Purple", 3 : "White"}
d7 = {1 : "Black", 2 : "Purple", 3 : "White"}

print cmp(d6, d7)
