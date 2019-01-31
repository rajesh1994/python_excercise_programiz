# 1. Any character except for a new line
import re
text = "google.com"

# Any Character except for a newline
print re.findall('', text)
print re.findall('.', text)
print re.findall('..', text)
print re.findall('...', text)
print re.findall('....', text)
print re.findall('.....', text)
print re.findall('......', text)
print re.findall('.......', text)
print re.findall('........', text)
print re.findall('.........', text)
print re.findall('..........', text)
print re.findall('...........', text)
