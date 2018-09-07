# They copy() method returns a shallow copy of the dictionary.

d1 = {1 : "One", 2 : "Two", 3 : "Three"}

print "*" * 145
print " " * 50, "1. Python Dictionary copy()"
print "Dictionary d1 = ", d1

d2 = d1.copy()
print "Dictionary is copied from dictionary d1 by using copy() function:"
print "Dictionary d2 = ", d2

# The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.

d3 = {1, 2, 3, 4, 5, 6, 7, 8}

print "*" * 145
print " " * 50, "2. Python Dictionary fromkeys()"
print "Dictionary d3 = ", d3
keys1 = dict.fromkeys(d3)

print "Dictionary with keys d3 = ", keys1

#  The get() method returns the value for the specified key if key is in dictionary.

d4 = {"Name" : "Phill", "Age" : 23, "Gender" : "M", }

print "*" * 145
print " " * 50, "3. Python Dictionary get()"
print "Dictionary d4 = ", d4
print "Name: ", d4.get("Name")
print "Age: ", d4.get("Age")
# Value is not provided
print "Salary: ", d4.get("Salary")
# Value is provided
print "Salary: ", d4.get("Salary", 100000)

# The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.

d5 = {"apple" : 3, "Banana" : 4, "Grapes" : 5}

print "*" * 145
print " " * 50, "4. Python Dictionary items()"
print "Dictionary d5 = ", d5
print "Dictionary d5 displays a list of dictionary's (key, value) tuple pairs: ", d5.items()

# The keys() method returns a view object that displays a list of all the keys in the dictionary.

d6 = {"name" : "Phill", "age" : 23, "gender" : "M"}
d7 = {}
print "*" * 145
print " " * 50, "5. Python Dictionary keys()"
print "Dictionary d6 = ", d6
print "Dictionary d7 = ", d7
print "Dictionary d6's keys are: ", d6.keys()
print "Dictionary d7's keys are: ", d7.keys()

# The values() method returns a view object that displays a list of all the values in the dictionary.

print "*" * 145
print " " * 50, "6. Python Dictionary values()"
print "Dictionary d6 = ", d6
print "Dictionary d7 = ", d7
print "Dictionary d6's values are: ", d6.values()
print "Dictionary d7's values are: ", d7.values()

# The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

d8 = {"name" : "Phill"}

print "*" * 145
print " " * 50, "7. Python Dictionary setdefault()"
print "Dictionary d8 = ", d8
# Key is not in the dictionary
salary = d8.setdefault("salary")
print "Dictionary d8 = ", d8
print "Salary: ", salary

# Key is not in the dictionary
# Default value is provided
age = d8.setdefault("age", 23)
print "Dictionary d8 = ", d8
print "Age: ", age
print "*" * 145
