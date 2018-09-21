# Create a text file in Python

file_write = open("testfile.txt", "r+")

file_write.write("Hello World\n")
file_write.write("This is our new text file ")
file_write.write("and this another.\n")
file_write.write("Why? Because we can.")

file_write.close()

