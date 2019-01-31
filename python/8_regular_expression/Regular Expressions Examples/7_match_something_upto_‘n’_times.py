# Match something upto n times
import re

dob1 = "18, Sep 2000"

# {n} Matches repeat n times.
print "*" * 145
print "Actual Value: ", dob1
print " " * 30, "1. {n} Matches repeat n times."
print "Matching exactly 4 characters: ", re.findall('\d{4}', dob1)
dob2 = "15, Aug 1947 & 1, Aug 2000"
print "\nActual Value: ", dob2
print "Matching exactly 2 to 4 characters: ", re.findall('\d{2,4}', dob2)
print "*" * 145
