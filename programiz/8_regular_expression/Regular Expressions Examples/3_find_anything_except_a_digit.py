# Find Anything except a digit
import re

dob = "16-June-1994"

print "*" * 145
print "Actual Value: ", dob
print "Find Anything except a digit from:", re.findall('\D+', dob)
print "*" * 145
