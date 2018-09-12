import sys
sys.setrecursionlimit(20000)

def sum(list):
    sum = 0
    
    # Add every number in the list
    for i in range(0, len(list)):
        sum = sum + list[i]
    
    # Return the sum
    return sum
print "Sum of the values are: ", sum([10, 30, 22, 8, 31])

