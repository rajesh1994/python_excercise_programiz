# Appending a text into the text file

file_append = open("testfile1.txt", "a")

file_append.write("\nOne more line has been included.")

print "*" * 145
print " " * 50, "1. Appending a text in a text file"
file_append = open("testfile1.txt", "r")
print file_append.read()
print "*" * 145
