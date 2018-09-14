# Import all names
"""
We can import all names(definitions) from a module using * operator.
"""

from math import *

print "*" * 145
print " " * 50, "1. Import all names"
print "The value of pi is", pi
print "*" * 145

"""
    We imported all the definitions from the math module.
    This makes all names except those beginnig with an underscore, visible in our scope.

    Importing everything with the asterisk (*) symbol is not a good programming practice. This can lead to duplicate definitions for an identifier.
    It also hampers the readability of our code.
"""
