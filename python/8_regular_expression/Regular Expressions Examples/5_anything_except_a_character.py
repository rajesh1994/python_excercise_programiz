# "Anything except a character"
import re

dob = "16, June 1994"

print "*" * 145
print "Actual Value: ", dob
print "Anything except a character:", re.findall('\W+', dob)
print "*" * 145
