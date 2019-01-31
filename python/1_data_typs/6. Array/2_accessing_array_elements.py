"""
Access elements of an Array:

    We can access individual elements of an array using index inside square brackets [].
Array Index

    Index is the position of element in an array. In Python, arrays are zero-indexed. This means, the element's position starts with 0 instead of 1.
"""

# Accessing elements of array using indexing

a1 = ["Apple", "Banana", "Cat"]

print "*" * 145
print " " * 50, "1. Accessing elements of array using indexing"
print "a1 = ", a1
print "a1[0] = ", a1[0]
print "a1[1] = ", a1[1]
print "a1[2] = ", a1[2]

"""
Negative Indexing

    Python programming supports negative indexing of arrays, something that is not available in arrays in most programming languages. This means the index value of -1 gives the last element, and -2 gives the second to last element of an array.
"""

# Accessing elements of array using negative indexing

a2 = [0, 1, 2, 3, 4, 5, 6, 7]

print "*" * 145
print " " * 50, "2. Accessing elements of array using negative indexing"
print "a2 = ", a2
print "a2[-1] = ", a2[-1]
print "a2[-2] = ", a2[-2]
print "a2[-3] = ", a2[-3]
print "a2[-4] = ", a2[-4]
print "a2[-5] = ", a2[-5]
print "a2[-6] = ", a2[-6]
print "a2[-7] = ", a2[-7]
print "a2[-8] = ", a2[-8]

"""
Find length of an Array

    Python arrays are just lists, so finding the length of an array is equivalent to finding length of a list in Python.
"""

# Find length of an array using len()

brands = ["Apple", "Coke", "Google", "Microsoft", "Toyota"]

print "*" * 145
print " " * 50, "3. Find length of an array using len()"
print "Length of array 'brands' = ", len(brands)

"""
Add an element to an Array

To add a new element to an array, we use append() method in Python.
"""

# Adding an element in an array using append()

a3 = ['a', 'b', 'c']
print "*" * 145
print " " * 50, "4. Adding an element in an array using append()"
print "Before appending value 'd' in array a3:"
print "a3 = ", a3

a3.append('d')

print "After appending value 'd' in array a3:"
print "a3 = ", a3

# Removing elements of an array using del, remove() and pop()

"""
Remove elements from an Array

Python's list implementation of array allows us to delete any elements from an array using del operator.

Similarly, we can also use remove() and pop() methods to remove elements in an array.
"""

colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]

print "*" * 145
print " " * 50, "5.Removing elements of an array using del, remove() and pop()"
print "Before removing, poping, poping array 'colors' as follow:"
print "colors = ", colors

del colors[3]
colors.remove("Red")
colors.pop(0)

print "After removing, poping, poping array 'colors' as follow:"
print "colors = ", colors

# Modifying elements of an array using Indexing 

"""
Modify elements of an Array

    We can change values of elements within an array using indexing and assignment operator (=). We select the position of any element using indexing and use assignment operator to provide a new value for the element.
"""

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]

print "*" * 145
print " " * 50, "6. Modifying elements of an array using Indexing"
print "Before modifiying array:"
print "fruits = ", fruits

fruits[1] = "Pineapple"
fruits[-1] = "Guava"

print "After modiying array:"
print "fruits = ", fruits

# Concatenating two arrays using + operator

concat = [1, 2, 3, 4]

print "*" * 145
print " " * 50, "7. Concatenating two arrays using + operator"
print "Before applying '+' in array:"
print "concat = ", concat

concat += [5, 6, 7]

print "After applying '+' operator in array:"
print "concat = ", concat

# Repeating elements in array using * operator

repeat = ["a"]

print "*" * 145
print " " * 50, "8. Repeating elements in array using * operator"
print "Before applying '*' in array:"
print "repeat = ", repeat

repeat = repeat * 5
print "After applying '*' in array:"
print "repeat = ", repeat

# Slicing an array using Indexing

"""
Slicing an Array:

    Python has a slicing feature which allows to access pieces of an array. We, basically, slice an array using a given range (eg. 2nd to 5th position), giving us elements we require. This is done by using indexes separated by a colon [x : y].

    We can use negative indexing with slicing too.
"""

fruits = ["Apple", "Banana", "Mango", "Grape", "Orange"]

print "*" * 145
print " " * 50, "9. Slicing an array using Indexing"
print "fruits = ", fruits
print "fruits[1 : 4] = ", fruits[1 : 4]
print "fruits[1 : ] = ", fruits[ : 3]
print "fruits[-4 : ] = ", fruits[-4 : ]
print "fruits[-3 : -1] = ", fruits[-3 : -1]
