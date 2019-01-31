# Python if...elif...else Statement

"""
    The elif is short for else if. It allows us to check for multiple expressions.

    If the condition for if is False, it checks the condition of the next elif block and so on.

    If all the conditions are False, body of else is executed.

    Only one block among the several if...elif...else blocks is executed according to the condition.

    The if block can have only one else block. But it can have multiple elif blocks.
"""

# In this program, we check if the number is positive or negative or zero & display appropriate message.

num = -7

print "*" * 143
print " " * 50, "1.Python if...elif...else Statement"

if num > 0:
    print num, "is a positive number."
elif num == 0:
    print num, "Zero"
else:
    print num, "is a negative number."
print "*" * 143
