# Raising an Exception:

# We can use "raise" to throw an exception if a condition occurs. The statement can be complemented with a custom exception.

x = int(raw_input("Enter a value for x: "))

if x > 5:
    raise Exception("x should not exceed 5. The value of x was: {}".format(x))

else:
    print "x = {}.".format(x)
