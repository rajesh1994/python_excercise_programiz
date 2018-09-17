# What is the use of break and continue in Python?

"""
    In Python, break and continue statements can alter the flow of a normal loop.

    Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

    The break and continue statements are used in these cases.
"""

# Python break statement

"""
    The break statement terminates the loop containing it.
    
    Control of the program flows to the statement immediately after the body of the loop.

    If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
"""
print "*" * 143
print " " * 50, "1. Python break statement"
for val in "String":
    if val == "i":
        break
    print val
print "The End"

# Python continue statement

"""
    The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
    Loop does not terminate but continues on with the next iteration.
"""
print "*" * 143
print " " * 50, "2. Python continue statement"
for val in "Batman":
    if val == "m":
        continue
    print val
print "The End"
print "*" * 143
