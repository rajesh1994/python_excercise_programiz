try:
    with open("file.log") as file:
        read_data = file.read()

except IOError as fnfe:
    print (fnfe)
