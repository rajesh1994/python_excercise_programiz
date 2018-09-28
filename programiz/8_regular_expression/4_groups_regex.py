# Regex groups
import re
print "*" * 145
print " " * 40, "1. Regex groups"
text = """101 COM Computers
205    MAT     Maths
189    ENG     English"""

# Extracting all course numbers

a = re.findall('[0-9]+', text)

print "1. Extracting all course numbers:"
print a, "\n"

# Extracting all course codes
b = re.findall('[A-Z]{3}', text)

print "2. Extracting all course codes:"
print b, "\n"

# Extracting all course names

c = re.findall('[a-zA-Z]{4,}', text)

print "Exctracting all course names:"
print c

# define the course text pattern groups and extract

course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([a-zA-Z]{4,})'

d = re.findall(course_pattern, text)
print "\nExtracting course number, course code, course name:"
print d
print "*" * 145
