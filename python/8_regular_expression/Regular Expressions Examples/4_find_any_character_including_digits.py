# Find any character, including digits
import re

dob = "16, June 1994"

print "*" * 145
print "Actual Value: ", dob
print "Find any character, including digits: ", re.findall('\w+', dob)
print "*" * 145
