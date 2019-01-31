import re

text = "101 COM Computer 205 MAT Maths 189 ENG English"
print text

a = re.compile("\d+")
b = a.findall(text)

print b
