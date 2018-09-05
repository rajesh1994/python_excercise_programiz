# The count() method returns the number of occurrences of an element in a tuple.
t1 = (1, 33, 34, 1, 88, 103, 22, 33, 1, 100, 3, 888, 654, 765, 100)
print "*" * 145
print "Tuple t1's elements are: ", t1

print "*" * 145
print " " * 50, "1. count()"
count_tuple = t1.count(1)
print "1 is appeared in the tuple t1 %s times."%count_tuple

# The index() method searches an element in a tuple and returns its index.
print "*" * 145
print " " * 50, "2. index()"
print "Index of element 100 in tuple t1 is: ", t1.index(100)
print "*" * 145

# The len() function returns the number of items (length) of an object.

print " " * 50, "3. len()"
print "Length of the tuple t1 is: ", len(t1)
print "*" * 145

# The max() method returns the largest element in an iterable or largest of two or more parameters.

print " " * 50, "4. max()"
print "Largest element in the tuple t1 is :", max(t1)
print "*" * 145

# The min() method returns the lowest element in an iterable or largest of two or more parameters.

print " " * 50, "5. min()"
print "Lowest element in the tuple t1 is :", min(t1)
print "*" * 145

# The sum() function adds the items of an iterable and returns the sum.
print " " * 50, "6. sum()"
print "Largest element in the tuple t1 is :", sum(t1)
print "*" * 145

# The sorted() method returns a sorted list from the given iterable.
print " " * 50, "7. sorted()"
print "Tuple t1 is sorted by ascending order as follow :", sorted(t1, reverse = 0)
print "Tuple t1 is sorted by ascending order as follow :", sorted(t1, reverse = 1)
print "*" * 145

# The enumerate() method adds counter to an iterable and returns it (the enumerate object).
t2 = ("apple", "Banana", "Cat", "Dove")
print " " * 50, "8. enumerate()"
e1 = tuple(enumerate(t2, start = 0))
print "Index and Values of tuple t2 is: ", e1
print "*" * 145

# Convert an iterable (list, string, set, dictionary) to a tuple.

l1 = [1, 2, 3, 4]
s1 = {5, 6, 7, 8}
print " " * 50, "9. tuple()"
print "List l1 is converted into tuple by using tuple() function: ", tuple(l1)
print "Set s1 is converted into tuple by using tuple() FUNCTION: ", tuple(s1)
print "*" * 145
