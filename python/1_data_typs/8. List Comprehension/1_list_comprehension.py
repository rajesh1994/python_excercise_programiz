# Iterating through a string Using List Comprehension
"""
    List comprehension is an elegant way to define and create lists based on existing lists.
"""
l1 = [letter for letter in 'human']
print "*" * 145
print " " * 50, "1. Iterating through a string Using List Comprehension"
print "l1 = ", l1

# Conditionals in List Comprehension

"""
    List comprehensions can utilize conditional statement to modify existing list (or other tuples).
    We will create list that uses mathematical operators, integers, and range().
"""

number_list = [x for x in range(20) if x % 2 == 0]
print "*" * 145
print " " * 50, "2. Conditionals in List Comprehension"
print "number_list = ", number_list

# Nested IF with List Comprehension

nest_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print "*" * 145
print " " * 50, "3. Nested IF with List Comprehension"
print "nest_list = ", nest_list

# if...else With List Comprehension
oe_list = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print "*" * 145
print " " * 50, "4. if...else With List Comprehension"
print "oe_list = ", oe_list
print "*" * 145

"""
Key Points to Remember

    List comprehension is an elegant way to define and create lists based on existing lists.
    List comprehension is generally more compact and faster than normal functions and loops for creating list.
    However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
    Remember, every list comprehension can be rewritten in for loop, but every for loop can not be rewritten in the form of list comprehension.

"""
