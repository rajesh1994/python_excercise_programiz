# Python Nested if statements

"""
    We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.

    Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting. This can get confusing, so must be avoided if we can.
"""

# In this porogram, we input the number & check if the number is positive or negative or zero & display the appropriate message.

# This time we use nested if

print "*" * 143
print " " * 50, "1. Python Nested if statements"
num = float(raw_input("Enter a number: "))

if num >= 0:
    if num == 0:
        print "Zero"
    else:
        print num, "is a positive number."
else:
    print num, "is a negative number."
print "*" * 143
