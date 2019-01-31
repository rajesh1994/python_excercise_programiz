# Nonlocal Variables
"""
    Nonlocal variable are used in nested function whose local scope is not defined.
    This means, the variable can be neither in the local nor the global scope.
    We use nonlocal keyword to create nonlocal variable.
"""

# Non Local variable works in python3 only.

def outer():
    x = "Local"
    
    def inner():
        nonlocal x
        x = "Non Local"
        print ("Inner: ", x)

    inner()
    print ("Outer: ", x)

outer()
