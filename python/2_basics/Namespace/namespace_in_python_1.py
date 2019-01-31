"""
What is a Namespace in Python?

    Namespace is a collection of names.

    In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

    Different namespaces can co-exist at a given time but are completely isolated.

    A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

    This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program.
    Each module creates its own global namespace.

    These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.

    Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it.
    
Here are a few examples of namespaces:

    Local Namespace: This namespace includes local names inside a function. This namespace is created when a function is called, and it only lasts until the function returns.

    Global Namespace: This namespace includes names from various imported modules that you are using in a project. It is created when the module is included in the project, and it lasts until the script ends.

    Built-in Namespace: This namespace includes built-in functions and built-in exception names.

"""

a = 2
print "*" * 145
print "id(2) is: ", id(2)

a = a + 1

print "*" * 145
print "id(a + 1) is: ", id(a)

print "id(a) is: ", id(3)
print "*" * 145

b = 2

print "id(2) is: ", id(2)
print "*" * 145
