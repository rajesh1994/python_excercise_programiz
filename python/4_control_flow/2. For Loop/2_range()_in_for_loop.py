# The range() function in for loop

"""
    We can use the range() function in for loops to iterate through a sequence of numbers.
    It can be combined with the len() function to iterate though a sequence using indexing.
"""

genre = ["Pop", "Rock", "Jazz"]

print "*" * 143
print " " * 50, "1. The range() function in for loop"
for i in range(len(genre)):
    print "I like ", genre[i]
print "*" * 143
