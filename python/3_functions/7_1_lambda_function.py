l1 = [1, 5, 4, 6, 8, 11, 3, 12]

l2 = list(filter(lambda x : (x%2 == 0), l1))

print "Using filter():"
print l2

l3 = [1, 5, 4, 6, 8, 11, 3, 12]

l4 = list(map(lambda x : (x * 2), l3))

print "using map():"
print l4
