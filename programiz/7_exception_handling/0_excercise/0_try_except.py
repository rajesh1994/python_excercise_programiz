# An example code for try...except concept in Python

print "*" * 50
print " " * 40, "1. Python handles exception using try .. except ..  block."
try:
    f = open("textfile.txt", "r")
    print f.read()
    f.close()

except IOError:
    print "File not found"
