# Class
"""
    A class is a blueprint for the object.

    We can think of class as an sketch of a parrot with labels.

    It contains all the details about the name, colors, size etc.

    Based on these descriptions, we can study about the parrot. Here, parrot is an object.
"""

# Object
"""
    An object (instance) is an instantiation of a class.

    When class is defined, only the description for the object is defined.

    Therefore, no memory or storage is allocated.
"""

class Parrot:
    # class attribute
    species = "bird"
    
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instansttiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 13)

# access the class attribute
print "*" * 145
print " " * 50, "1. Class & Objects in Python"
print "Blu is a {}".format(blu.__class__.species)
print "Woo is a {}".format(woo.__class__.species)

# access the instance attribute
print "{} is {} years old".format(blu.name, blu.age)
print "{} is {} years old".format(woo.name, woo.age)
print "*" * 145
