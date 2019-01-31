# The AssertionError Exception
"""
    Instead of waiting for a program to crash midway, you can also start by making an assertion in Python.

    We assert that a certain condition is met.

    If this condition turns out to be True, then that is excellent! The program can continue.
    
    If the condition turns out to be False, you can have the program throw an AssertionError exception.
"""

import sys

assert ("linux" in sys.platform), "This code runs on linux only"
