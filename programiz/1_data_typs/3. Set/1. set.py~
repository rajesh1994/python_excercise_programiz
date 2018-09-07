"""
What is a set in Python?

    A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).

    However, the set itself is mutable. We can add or remove items from it.

    Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
How to create a set?

    A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().

    It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.
    
    Creating an empty set is a bit tricky.

    Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set() function without any argument.
"""

s1 = set()

s2 = {1, 5, 3, 4, 2, 0}

s3 = {1, 10, 11, 17, 3.089, 3.14, ("Parrot", "Lion")}

print "*" * 145
print "Set s1 is empty: ", s1

print "*" * 145
print "Set s2 contains 6 elements: ", s2

print "*" * 145
print "Set s3 contains integer, float, list, tuple ect.: ", s3
print "*" * 145

"""
How to change a set in Python?

Sets are mutable. But since they are unordered, indexing have no meaning.

We cannot access or change an element of set using indexing or slicing. Set does not support it.

We can add single element using the add() method and multiple elements using the update() method. The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.
"""

a = s1.add(9)
print "Adding an element in the set s1", s1
print "*" * 145

u = s1.update([20, 38, 43, 102, 201])
print "Updating set s1: ", s1
print "*" * 145

"""
How to remove elements from a set?

A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.

We can also remove all items from a set using clear().
"""

s4 = {"Birds", "Animals", "Ship", "Plan", "Ice Cream"}
print "Set s4 is: ", s4


d = s4.discard("Ship")
print "After discarding value 'Ship' from set s4: ", s4

r = s4.remove("Plan")
print "After removing value 'Plan' from set s4: ", s4
print "*" * 145

s5 = {"Pappaya", "Banana", "Grape"}

c = s5.clear()

print "After clearing the set s5: ", s5
print "*" * 145

