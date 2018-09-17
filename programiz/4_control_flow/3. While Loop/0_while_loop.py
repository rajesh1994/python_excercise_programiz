# What is while loop in Python?

"""
    The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

    We generally use this loop when we don't know beforehand, the number of times to iterate.

    In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.

    In Python, the body of the while loop is determined through indentation.

    Body starts with indentation and the first unindented line marks the end.

    Python interprets any non-zero value as True. None and 0 are interpreted as False.
"""

# Program to add natural numbers upto sum = 1 + 2 + 3 + ... + n

print "*" * 143
print " " * 50, "1. While loop in python"
# To take input from the user
n = int(raw_input("Enter the number: "))

# Initialize sum & counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1   # Update the Counter

# Print the sum
print "The sum is", sum
print "*" * 143
