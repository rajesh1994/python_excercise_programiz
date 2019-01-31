# The try and except Block: Handling Exceptions
"""
    The try and except block in Python is used to catch and handle exceptions.
    
    Python executes code following the try statement as a normal part of the program.
    
    The code that follows the except statement is the programs response to any exceptions in the preceding try clause.

    As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error.
    
    This exception error will crash the program if it is unhandled.
    
    The except clause determines how your program responds to exceptions.
"""

def linux_interaction():
    assert("linux" in sys.platform), "Function can only run linux system."
    print "Doing Something"
