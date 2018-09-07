# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

l1 = ["Apple", "Banana", "Coconut", "Dream", "Egypt", "Flower"]

print "-" * 145
print "The actual data in list l1 is: ", l1

print "-" * 145
print "The values at index 0, 1, 2, 3, 4, 5 in list l1 are: ", l1[0], l1[1], l1[2], l1[3], l1[4], l1[5]

print "-" * 145
print "The values at index 0, -1, -2, -3, -4, -5 in list l1 are: ", l1[0], l1[-1], l1[-2], l1[-3], l1[-4], l1[-5]
print "-" * 145
