# Methods

"""
    Methods are functions defined inside the body of a class.

    They are used to define the behaviors of an object.
"""

class Parrot:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods/functions
print "*" * 145
print " " * 50, "1. Methods/Functions in Python"
print blu.sing("'Happy'")
print blu.dance()
print "*" * 145
