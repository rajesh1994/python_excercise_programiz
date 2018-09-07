"""
Python Variable Scope:

    Although there are various unique namespaces defined, we may not be able to access all of them from every part of the program. The concept of scope comes into play.

    Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

    At any given moment, there are at least three nested scopes.

        Scope of the current function which has local names
        Scope of the module which has global names
        Outermost scope which has built-in names

    When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

    If there is a function inside another function, a new scope is nested inside the local scope.
"""

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print "a = ", a
    
    inner_function()
    print "a = ", a

a = 10
outer_function()
print "a = ", a
