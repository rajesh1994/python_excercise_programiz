# Encapsulation

"""
    Using OOP in Python, we can restrict access to methods and variables.
    This prevent data from direct modification which is called encapsulation.
    In Python, we denote private attribute using underscore as prefix i.e single ( _ ) or double ( __).
"""

class Computer:

    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print "Selling price: {}".format(self.__maxprice)
        
    def setMaxPrice(self, price):
        self.__maxprice = price

print "*" * 145
print " " * 50, "1. Encapsulation in python"
c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
print "*" * 145
