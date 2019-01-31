# Reading a text file in Python

# Reading a whole text file in Python
file_read = open("testfile.txt", "r")

print "*" * 145
print " " * 50, "1. Reading a whole text file in Python"
print file_read.read()

file_read.close()

# Reading a certain number of characters from a text file
file_read = open("testfile.txt", "r")

print "*" * 145
print " " * 50, "2. Reading a certain number of characters from a text file"
print file_read.read(5)

file_read.close()

# Reading a certain number of lines from a text file
# Note : By calling readline() two times, you can read the two first lines:
file_read = open("testfile.txt", "r")                                                                                                                                                                                                                                                                                   

print "*" * 145
print " " * 50, "3. Reading a lines of text from a text file"
print file_read.readline()
print file_read.readline()

# Reading every line in the file seperated by comma(,), highlighted by double quotes("")

file_read = open("testfile.txt", "r")

print "*" * 145
print " " * 50, "4. Reading every line in the file seperated by comma(,), highlighted by double quotes("")"
print file_read.readlines()
print "*" * 145
