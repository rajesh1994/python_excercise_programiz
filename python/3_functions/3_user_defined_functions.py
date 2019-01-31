# What are user-defined functions in Python?
"""
    Functions that we define ourselves to do certain specific task are referred as user-defined functions.
    The way in which we define and call functions in Python are already discussed.

    Functions that readily come with Python are called built-in functions.
    If we use functions written by others in the form of library, it can be termed as library functions.

    All the other functions that we write on our own fall under user-defined functions.
    So, our user-defined function could be a library function to someone else.
"""

# Advantages of user-defined functions

"""
    User-defined functions help to decompose a large program into small segments which makes program easy to understand, maintain and debug.
    If repeated code occurs in a program. Function can be used to include those codes and execute when needed by calling that function.
    Programmars working on large project can divide the workload by making different functions.
"""

def add_numbers(x, y):
    sum = x + y
    return sum

n1 = 10
n2 = 20

print "The sum equal to ", add_numbers(n1, n2)
