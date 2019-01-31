a = [1, 2, 3]

try:
    print "Second element = %d" %(a[1])
    
    # Throws an error since there are only 3 elements in the list
    print "Fourth element = %d" %(a[5])

except IndexError:
    print "An Error Occured."
