# What are lambda functions in Python?

"""
    In Python, anonymous function is a function that is defined without a name.
    While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
    Hence, anonymous functions are also called lambda functions.
    Lambda functions can have any number of arguments but only one expression.
    The expression is evaluated and returned.
    Lambda functions can be used wherever function objects are required.
"""
value = lambda x : x ** x

a = value(5)
l = len(str(a))
print "Ans :", a
print "Length = ", l

# Use of Lambda Function in python

"""
    We use lambda functions when we require a nameless function for a short period of time.
    In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
    Lambda functions are used along with built-in functions like filter(), map() etc.
"""
