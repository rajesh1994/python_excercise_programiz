"""
What is recursion in Python?

    Recursion is the process of defining something in terms of itself.

    A physical world example would be to place two parallel mirrors facing each other.
    Any object in between them would be reflected recursively.
"""


# Python Recursive Function:

"""
    We know that in Python, a function can call other functions.
    It is even possible for the function to call itself.
    These type of construct are termed as recursive functions.
    Following is an example of recursive function to find the factorial of an integer.
    Factorial of a number is the product of all the integers from 1 to that number.
    For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
"""

import sys
sys.setrecursionlimit(20000)

def fact(x):
    """
    This is the recursive function
    to find the factorial of an integer.
    """
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

num = 50
print "The factorial of", num, "is", fact(num)

# Advantages of Recursion

"""
    Recursive functions make the code look clean and elegant.
    A complex task can be broken down into simpler sub-problems using recursion.
    Sequence generation is easier with recursion than using some nested iteration.
"""

# Disadvantages of Recursion

"""
    Sometimes the logic behind recursion is hard to follow through.
    Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    Recursive functions are hard to debug.
"""
