# Global Variables
"""
    In Python, a variable declared outside of the function or in global scope is known as global variable.
    This means, global variable can be accessed inside or outside of the function.
"""

# Local Variables
"""
    A variable declared inside the function's body or in the local scope is known as local variable.
"""

# Introduction to global Keyword
"""
    In Python, global keyword allows you to modify the variable outside of the current scope. 
    It is used to create a global variable and make changes to the variable in a local context.
"""

# The basic rules for global keyword in Python are:
"""
    When we create a variable inside a function, it is local by default.
    When we define a variable outside of a function, it is global by default. You do not have to use global keyword.
    We use global keyword to read and write a global variable inside a function.
    Use of global keyword outside a function has no effect.
"""

# Global Variable
x = "Global"
print "*" * 145
print " " * 50, "1. Types of variable in Python's function"
print "Before using global keyword:"
print x
def foo():
    global x
    # Local Variable
    y = "Local"  
    x = "Global Variable"
    print "*" * 145
    print y
    print "*" * 145
    print "After using global keyword:"
    print x
    print "*" * 145
foo()
