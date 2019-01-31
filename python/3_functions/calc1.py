# The import statement
"""
    We can use any Python source file as a module by executing an import statement in some other Python source file.
    When interpreter encounters an import statement, it imports the module if the module is present in the search path.
    A search path is a list of directories that the interpreter searches for importing a module.
    For example, to import the module calc.py, we need to put the following command at the top
"""

import 10_1_calc

print add(10, 3)
