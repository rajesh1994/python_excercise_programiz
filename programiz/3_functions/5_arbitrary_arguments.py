# Python Arbitrary Arguments

"""
Sometimes, we do not know in advance the number of arguments that will be passed into a function.Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.

In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.
"""

def greet(*names):
    
    """
    This function greets all
    the persons in the same tuple.
    """
    # names is a tuple with arguments
    for name in names:
        print "Hello", name

greet("Sam", "Sathya", "Anoop", "Karthick", "Prakash")
