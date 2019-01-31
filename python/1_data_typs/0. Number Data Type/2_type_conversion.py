# Type Conversion
"""
    We can convert one type of number into another. This is also known as coercion.
    Operations like addition, subtraction coerce integer to float implicitly (automatically), if one of the operand is float.
    We can also use built-in functions like int(), float() and complex() to convert between types explicitly.
    These function can even convert from strings.
"""

a = 2 + 5.0

print "*" * 145
print " " * 50, "1. Imteger Type Conversion"
print "a = 2 + 5.0 = ", a

b = int(3.14)

print "*" * 145
print " " * 50, "2. Integer Type Conversion"
print "b = ", b

c = float(-9)

print "*" * 145
print " " * 50, "3. float Type Conversion"
print "c = ", c

d = complex("3+8j")

print "*" * 145
print " " * 50, "4. Complex Type Conversion"
print "d = ", d
print "*" * 145

"""
When to use Decimal instead of float?

We generally use Decimal in the following cases.

    When we are making financial applications that need exact decimal representation.
    When we want to control the level of precision required.
    When we want to implement the notion of significant decimal places.
    When we want the operations to be carried out like we did at school

"""
