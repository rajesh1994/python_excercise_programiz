"""
What is Nested Dictionary in Python?

    In Python, a nested dictionary is a dictionary inside a dictionary. It's a collection of dictionaries into one single dictionary.

"""

people = {1 : {"name" : "John Pope", "age" : 24, "gender" : "M"},
          2 : {"name" : "Marie John", "age" : 23, "gender" : "F"}}
print "*" * 145
print "1. Creating nested dictionary:"
print "people = ", people

"""
Access elements of a Nested Dictionary

    To access element of a nested dictionary, we use indexing [] syntax in Python.

"""
print "*" * 145
print "2. Accessing elements from dictionary:"
print people[1]["name"]
print people[1]["age"]
print people[1]["gender"]

# How to change or add elements in a nested dictionary?
people[3] = {}
people[3]["name"] = "Luna"
people[3]["age"] = 21
people[3]["gender"] = "F"
people[3]["martial status"] = "Single"

print "*" * 145
print "3. Adding new dictionary inside the people dictionary:"
print "people = ", people

# Add another dictionary to the nested dictionary
people[4] = {"name" : "Peter", "age" : 22, "gender" : "F", "martial status" : "Single"}

print "*" * 145
print "4. Adding another dictionary to the nested dictionary:"
print "people[4] = ", people[4]

"""
Delete elements from a Nested Dictionary

    In Python, we use 'del' statement to delete elements from nested dictionary.
"""

del people[3]["martial status"]
del people[4]["martial status"]

print "*" * 145
print "5. Delete elements from a Nested Dictionary"
print "people = ", people
print "people[3]", people[3]
print "people[4]", people[4]

# How to delete dictionary from a nested dictionary?
del people[3]
del people[4]

print "*" * 145
print "6. Delete dictionary from a nested dictionary"
print "people = ", people

"""
Key Points to Remember:

   >> Nested dictionary is an unordered collection of dictionary
   >> Slicing Nested Dictionary is not possible.
   >> We can shrink or grow nested dictionary as need.
   >> Like Dictionary, it also has key and value.
   >> Dictionary are accessed using key.

"""
