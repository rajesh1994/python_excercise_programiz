__metaclass__ = type
# Inheritance
"""
    Inheritance is a way of creating new class for using details of existing class without modifying it.

    The newly formed class is a derived class (or child class).    

    Similarly, the existing class is a base class (or parent class).
"""

# parent class
class Bird(object):

    def __init__(self):
        print "Parent class:"
        print "Bird is ready"
        
    def whoisThis(self):
        print "Bird"
        
    def swim(self):
        print "Swim Faster"

# child class
class Penguin(Bird):
    
    def __init__(self):
        # call super() function
        #super(self).__init__()
        print "\nChild class:"
        print "Penguin is ready"
        
    def whoisThis(self):
        print "Penguin"
        
    def run(self):
        print "Run faster"

# instantiate the object
print "*" * 145
print " " * 50, "1. Inheritance in Python"
bird = Bird()
bird.whoisThis()
bird.swim()

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
print "*" * 145
