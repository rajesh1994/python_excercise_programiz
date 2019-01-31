# Inheritance in Python

"""
    Inheritance is the capability of one class to derive or inherit the properties from some another class.
"""
    
# The benefits of inheritance are:
"""
    It represents real-world relationships well.

    It provides reusability of a code. We do not have to write the same code again and again.
   
    Also, it allows us to add more features to a class without modifying it.
    
    It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
"""

# Python program to demonstrate inheritance
# Base/Super class. Note object in bracket.

class Person(object):
    # Constructor
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
    # Co check if this person is employee
    def isEmployee(self):
        return False
        
# Derived/Sub class. Note Person in bracket
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

print "*" * 145
print " " * 50, "1. Inheritance in Python"
# creation of an object variable or an instance 
emp = Person("Rahul")
# calling a function of the class Person using its instance
print emp.getName(), emp.isEmployee()

# creation of an object variable or an instance 
emp = Employee("Pradeep")
# calling a function of the class Person using its instance
print emp.getName(), emp.isEmployee()
print "*" * 145
