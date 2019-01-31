# Substitute one text with another using regex

# Define the text
import re
text = """101     COM \t Computers
205     MAT \t Maths
189     ENG \t English"""

print "*" * 145
print " " * 40, "1. Substitute one text with another using regex\n"
print "Unordered text:"
print text

regex = re.compile("((?!\n)\s+)")

print "\n", "Ordered text:"
print (regex.sub(" ",text))
print "*" * 145
