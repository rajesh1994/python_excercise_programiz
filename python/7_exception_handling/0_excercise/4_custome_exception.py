# Creating custom exception class
"""
You can create a custom exception class by Extending BaseException  class or subclass of BaseException.
"""

def enterage(age):
    if age < 0:
        raise NegativeAgeException("Only positive integers are allowed")
    
    if age % 2 == 0:
        print "age is even"
    
    if age % 2 == 1:
        print "age id odd"

try:
    num = int(raw_input("Enter your age: "))
    enterage(num)

except NegativeAgeException:
    print "Only positive integers are allowed"

except:
    print "Something else"
