"""
What is dictionary in Python?

    Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.

    Dictionaries are optimized to retrieve values when the key is known.

"""
"""
How to create a dictionary?

    Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.

    An item has a key and the corresponding value expressed as a pair, key: value.

    While values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.
"""

# Empty dictionary
d1 = {}

# Dictionaries with integer keys
d2 = {1 : "Apple", 2 : "Banana", 3 : "Cat"}

# Dictionaries with mixed keys
d3 = {"name" : "Joker", 2 : [1, 2, 3, 4]}

# Using dict() to assign the values inside the dictionary
d4 = dict({1 : "Apple", 2 : "Banana"})

# From sequence having each item as a pair
d5 = dict({(1, "Apple"), (2, "Banana")})

print "*" * 145
print " " * 50, "1. Introduction to Dictionaries"
print "*" * 145
print "Empty dictionary: d1 = ", d1

print "*" * 145
print "Dictionary with integer keys: d2 = ", d2

print "*" * 145
print "Dictionary with mixed keys: d3 = ", d3

print "*" * 145
print "Dictionary with dict() function: d4 = ", d4

print "*" * 145
print "Dictionary from sequence having each item as a pair: d5 = ", d5
print "*" * 145
