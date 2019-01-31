"""
What is a function in Python?

    In Python, function is a group of related statements that perform a specific task.

    Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

    Furthermore, it avoids repetition and makes code reusable.
"""

def absolute_value(num):
    """ This function returns the absolute
    value of the entered number."""
    if num >= 0:
        return num
    else:
       return -num

print "Absolute value of 2 is: ", absolute_value(2)
print "Absolute value of -2 is: ", absolute_value(-2)
