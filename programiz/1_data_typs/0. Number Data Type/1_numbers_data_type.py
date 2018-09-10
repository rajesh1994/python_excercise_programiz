# Number Data Type in Python
"""
    Python supports integers, floating point numbers and complex numbers. They are defined as int, float and complex class in Python.

    Integers and floating points are separated by the presence or absence of a decimal point. 5 is integer whereas 5.0 is a floating point number.

    Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

    We can use the type() function to know which class a variable or a value belongs to and isinstance() function to check if it belongs to a particular class.
"""

a = 5
print "*" * 145
print " " * 50, "1. Integer Data Type"
print type(a)
print "a = ", a
print "Is it a integer data type?", isinstance(a, int)

b = 5.0

print "*" * 145
print " " * 50, "2. Float Data Type"
print type(b)
print "b = ", b
print "Is it a float data type?", isinstance(b, float)

c = 4+5j

print "*" * 145
print " " * 50, "3. Complex Data Type"
print type(c)
print "c = ", c
print "Is it a complex data type?", isinstance(c, complex)
print "*" * 145
