# In this program, three different variables a are defined in separate namespaces and accessed accordingly.

def outer_function():
    global a
    a = 20
    
    def inner_function():
        global a
        a = 30
        print "*" * 145
        print "a = ", a
        print "*" * 145
                
    inner_function()
    print "a = ", a
    print "*" * 145

a = 10
outer_function()
print "a = ", a
print "*" * 145

# Here, all reference and assignment are to the global a due to the use of keyword global.
