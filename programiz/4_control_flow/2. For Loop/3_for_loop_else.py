# for loop with else

"""
    A for loop can have an optional else block as well.

    The else part is executed if the items in the sequence used in for loop exhausts.

    break statement can be used to stop a for loop. In such case, the else part is ignored.

    Hence, a for loop's else part runs if no break occurs.
"""

digits = [0, 1, 2, 3, 4, 5]

print "*" * 143
print " " * 50, "1. for loop with else part"
for i in digits:
    print i
else:
    print "No items left"
print "*" * 143

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
