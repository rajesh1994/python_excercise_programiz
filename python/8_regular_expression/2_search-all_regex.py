# Define the text
import re
text = """COM Computers 205 MAT Maths 189"""

num = re.compile("\d+")
a = num.search(text)
print "Starting Position: ", a.start()
print "Ending Position:", a.end()
print text[a.start():a.end()]
