# Python Default Arguments

"""
Function arguments can have default values in Python.

We can provide a default value to an argument by using the assignment operator (=).
"""

def greet(name, msg = "Good Morning!"):
    """
    This function greet to
    the person with the
    provided message.
    """
    print "Hello", name, ",", msg

print "*" * 145
greet("Prakash")
greet("Bruce Wayne", "How do you do?")
print "*" * 145
