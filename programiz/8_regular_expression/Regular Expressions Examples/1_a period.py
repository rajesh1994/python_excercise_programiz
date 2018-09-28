# A period
import re

text = "google.com"

print re.findall('\.', text)
print re.findall('[^\.]', text)
