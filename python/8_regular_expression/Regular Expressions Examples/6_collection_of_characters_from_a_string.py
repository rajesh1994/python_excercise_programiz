# Finding collection of characters from a string
import re

dob = "16, June 1994, 04, December 1996"

print "*" * 145
print " " * 30, "1. {n} Matches repeat n times."
print "Actual Value: ", dob
# [] Matches any character inside
print "Finding collection of characters from a string:", re.findall('[A-Za-z]+', dob)
print "*" * 145
