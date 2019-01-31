# greedy matching in regex
import re

text = "<body> Regex Greedy matching example </body>"

g_match = re.findall('<.*>', text)

print "*" * 145
print " " * 40, "1. Greedy matching in regex"
print "Actual text = ", text
print "Greedy matching in regex:"
print g_match
print "*" * 145
