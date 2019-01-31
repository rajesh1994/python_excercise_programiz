# Using Exception objects
"""
    Now you know how to handle exception, in this section we will learn how to access exception object in exception handler code.
    
    You can use the following code to assign exception object to a variable.
    
    As you can see you can store exception object in variable ex . Now you can use this object in exception handler code
"""

try:
    number = eval(raw_input("Enter a number: "))
    print "The number entered is: ", number

except NameError as ex:
    print "Exception: ", ex
