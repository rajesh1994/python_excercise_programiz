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
    
    def __sub__(self, another_circle):
        return Circle(self.__radius - another_circle.__radius)
    
    def __mul__(self, another_circle):
        return Circle(self.__radius * another_circle.__radius)
    
    def __mod__(self, another_circle):
        return Circle(self.__radius % another_circle.__radius)
    
    def __gt__(self, another_circle):
        return Circle(self.__radius > another_circle.__radius)
    
    def __lt__(self, another_circle):
        return Circle(self.__radius < another_circle.__radius)
    
    def __le__(self, another_circle):
        return Circle(self.__radius <= another_circle.__radius)
    
    def __ge__(self, another_circle):
        return Circle(self.__radius >= another_circle.__radius)
    
    def __str__(self):
        return "Circle with radius " + str(self.__radius)
    
print "*" * 145
print " " * 50, "1. Python Operator Overloading"
c1 = Circle(10)
print "Circle1 radius = ", c1.getRadius()

c2 = Circle(15)
print "Circle2 radius = ", c2.getRadius()

c3 = c1 + c2
print "\nUsing __add__ method:"
print c3.getRadius()

c4 = c1 - c2
print "\nUsing __sub__ method:"
print c4.getRadius()

c5 = c1 * c2
print "\nUsing __mul__ method:"
print c5.getRadius()

c6 = c1 % c2
print "\nUsing __mod__ method:"
print c6.getRadius()

c7 = c1 > c2
print "\nUsing __gt__ method:"
print c7.getRadius()

c8 = c1 < c2
print "\nUsing __lt__ method:"
print c8.getRadius()

c9 = c1 >= c2
print "\nUsing __ge__ method:"
print c9.getRadius()

c10 = c1 <= c2
print "\nUsing __le__ method:"
print c10.getRadius()

print "\nUsing __str__ method:"
print c3
print "*" * 145
