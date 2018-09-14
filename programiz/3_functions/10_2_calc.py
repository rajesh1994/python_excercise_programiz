# The import statement
"""
    We can use any Python source file as a module by executing an import statement in some other Python source file.
    When interpreter encounters an import statement, it imports the module if the module is present in the search path.
    A search path is a list of directories that the interpreter searches for importing a module.
    For example, to import the module calc.py, we need to put the following command at the top
"""

import calc

sum = calc.add(10, 3)
sub = calc.sub(10, 3)

print "*" * 145
print " " * 50, "1. Python Modules"
print "Sum of two numbers: ", sum
print "Diffrence of two numbers: ", sub
print "*" * 145
