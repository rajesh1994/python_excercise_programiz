# Match 1 or more occurrences
import re

values0 = "So Google is awesome."
print "*" * 145
print "Match 1 or more occurrences"
print "Actual Values: ", values0
print re.findall(r'Go+gle', values0)
print "*" * 145

# Match any number of occurrences (0 or more times)
values1 = "Pilani"

print "Actual Values: ", values1
print re.findall(r'Pi*lani', values1)
print "*" * 145
# Match exactly zero or one occurrence
values2 = "Color Color"

print "Actual Values: ", values2
print re.findall(r'Colo?r', values2)
print "*" * 145
