# What is for loop in Python?

"""
    The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
    Iterating over a sequence is called traversal.
"""
# Program to find sum of all numbers in the list

# List of Numbers
l1 = [4, 3, 1, 2, 6, 4, 7, 9, 10, 18, 22, 100, 201]

# Variable to store the sum
sum = 0

# Iterate over the list
for val in l1:
    sum = sum + val

print "*" * 143
print " " * 50, "1. for loop in Python"
print "The sum is ", sum
print "*" * 143
