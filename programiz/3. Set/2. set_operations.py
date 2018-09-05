"""
Python Set Operations:

Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference. We can do this with operators or methods.
"""

s1 = {0, 1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8, 9}
s3 = {"Apple", "Banana", "Cat", "Dove", "Eat"}
s4 = {"Dove", "Eat", "Food", "Good", "Instagram"}

print "*" * 140
print " " * 50, "1. Set Union"

# Union of A and B is a set of all elements from both sets.

# Union is performed using | operator. Same can be accomplished using the method union().

print "Union of set s1 and s2: ", s1 | s2 # By using union operator.
print "Union of set s3 and s4: ", s3.union(s4) # By using union function.
print "*" * 140

#Intersection of A and B is a set of elements that are common in both sets.

#Intersection is performed using & operator. Same can be accomplished using the method intersection().

print " " *50, "2. Set Intersection" 
print "Set set s1 = %s & s2 = %s " %(s1, s2)
print "Intersection of set s1 and s2: ", s1 & s2 # By using intersection operator.
print "Set s3 = %s & s4 = %s " %(s3, s4)
print "Intersection of set s3 and s4: ", s4.intersection(s3) # By using intersection function.
print "*" * 140

"""
Difference of A and B (A - B) is a set of elements that are only in A but not in B.

Similarly, B - A is a set of element in B but not in A.

Difference is performed using - operator. Same can be accomplished using the method difference().
"""

print " " *50, "3. Set Difference" 
print "Set set s1 = %s & s2 = %s " %(s1, s2)
print "Set difference of set (s1 - s2): ", s1 - s2 # By using difference operator.
print "Set s3 = %s & s4 = %s " %(s3, s4)
print "Set difference of set (s4 - s3)", s4 - s3 # By using difference function.
print "*" * 140

"""
Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.

Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().
"""

print " " *50, "4. Set Symmetric Difference" 
print "Set set s1 = %s & s2 = %s " %(s1, s2)
print "Symmetric Difference of (s1 - s2): ", s1 ^ s2
print "Set s3 = %s & s4 = %s " %(s3, s4)
print "Symmetric Difference of (s4 - s3): ", s4 ^ s3
print "*" * 140
