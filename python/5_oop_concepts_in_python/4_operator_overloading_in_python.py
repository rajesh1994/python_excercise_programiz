# Python Operator Overloading
"""
    You have already seen you can use +  operator for adding numbers and at the same time to concatenate strings.

    It is possible because +  operator is overloaded by both int  class and str  class.

    The operators are actually methods defined in respective classes.
    
    Defining methods for operators is known as operator overloading.
    
    For e.g. To use +  operator with custom objects  you need to define a method called __add__  .
"""

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def setRadius(self, radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
print "*" * 145
print " " * 50, "1. Python Operator Overloading"
c1 = Circle(4)
print "Circle1 radius = ", c1.getRadius()

c2 = Circle(5)
print "Circle2 radius = ", c2.getRadius()

# This is become possible because we have overloaded + operator by adding a method __add__
c3 = c1 + c2
print "\nAdding two circle's radius by using metod __add__"
print "Two circle's radius = ", c3.getRadius()
print "*" * 145
