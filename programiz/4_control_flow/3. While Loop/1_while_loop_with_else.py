# while loop with else

"""
    Same as that of for loop, we can have an optional else block with while loop as well.

    The else part is executed if the condition in the while loop evaluates to False.

    The while loop can be terminated with a break statement.
    
    In such case, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.
"""

# Example to illustrate the use of else statement with the while loop

counter = 0

print "*" * 143
print " " * 50, "1. While loop with else statement"
while counter < 3:
    print "Inside loop"
    counter = counter + 1
else:
    print "Inside else"
print "*" * 143
