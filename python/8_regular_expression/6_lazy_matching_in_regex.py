# lazy matching in regex
import re

text = "<body> Regex Lazy matching example </body>"

l_match = re.findall('<.*?>', text)

print "*" * 145
print " " * 40, "1. Lazy matching in regex"
print "Actual text = ", text
print "Lazy matching in regex:"
print l_match
print "*" * 145
