s1 = {1, 2, 3, 4, 5, 6, 7, 8}

# The set add() method adds a given element to a set. If the element is already present, it doesn't add any element.
print "*" * 145
print " " * 50, "Set Functions"
print "*" * 145
print " " * 50, "1. add() function"
a = s1.add(9)
print "After adding an element in the set s1: ", s1
print "*" * 145

# The copy() method returns a shallow copy of the set.
# A set can be copied using = operator in Python.

print " " * 50, "2. copy() function"
s2 = s1
print "Set s2 is copied from set s1: ", s2
print "*" * 145

# The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
print " " * 50, "3. isdisjoint() function"

s3 = {10, 11, 12, 13}
s4 = {14, 15, 16, 17}
print "s3 = %s & s4 = %s" %(s3, s4)
print "Are set s3 & s4 are disjoint set? ", s3.isdisjoint(s4)
print "*" * 145

# The issubset() method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
print " " * 50, "4. issubset() function"

s5 = {10, 11, 12, 13}
s6 = {10, 11, 12, 13, 14, 15, 16, 17}
print "s5 = %s & s6 = %s" %(s5, s6)
print "Are set s5 & s6 are subset? ", s3.isdisjoint(s4)
print "*" * 145

