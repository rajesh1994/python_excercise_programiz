l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11, 12, 13, 14]
l3 = [15, "Boy", "Girl", "Tree", "10-10-2019", "Chennai"]
l4 = ["Monday", "Tuesday", "Wedneday", "Thursday", "Friday"]
l5 = ["integer", "float", "double", "string"]
l6 = [33, 100, 76, 12, 99, 103, 1777, 2, 40, 22]
l7 = [100, 401, 345, 74, 100, 55, 47, 74, 401, 100, 47]
l8 = ["Apple", "Ball", "Catch", "DRS", "Eat", "Food"]

# The append() method adds an item to the end of the list.
print "-" * 145
print "Before applying append() function in list l1: ", l1
append_list = l1.append(11)
print "The appended list is: ", l1
print "-" * 145

# The insert() method inserts the element to the list at the given index.
print "Before applying insert() function in list l4 is: ", l4
list_insert1 = l4.insert(0, "Sunday")
list_insert2 = l4.insert(6, "Saturday")
print "After applying insert() function in list l4 is: ", l4
print "-" * 145

# The extend() extends the list by adding all items of a list (passed as an argument) to the end.
print "Before applying extend() function in list l1: ", l1
list_extend = l1.extend(l2)
print "The extended l1 list is: ", l1
print "The length of the list l1 is: ", len(l1)
print "-" * 145

#The remove() method searches for the given element in the list and removes the first matching element.
print "Before applying remove() function in list l3: ", l3
remove_element_from_list = l3.remove(15)
print "After applying remove() function in list l3: ", l3
print "-" * 145

"""# The clear() method removes all items from the list.
print "-" * 145
print "Before applying clear() function in list l5: ", l5
clear_list = l5.clear()
print "After applying  clear() function in list l5: ", l5
print "-" * 145"""

"""In simple terms, index() method finds the given element in a list and returns its position.

However, if the same element is present more than once, index() method returns its smallest/first position.

Note: Index in Python starts from 0 not 1."""
list_index = l1.index(6)
print "Index of value 6 is: ", list_index
print "-" * 145

# The count() method returns the number of occurrences of an element in a list.
print "The list l7 is: ", l7
list_count1 = l7.count(100)
print "The count of 100 is: ", list_count1

list_count2 = l7.count(74)
print "The count of 74 is: ", list_count2
print "-" * 145

# The sort() method sorts the elements of a given list in a specific order - Ascending or Descending.
sorted_list_asc = l6.sort()
print "List is sorted by ascending order: ", l6
print "-" * 145

sorted_list_des = l6.sort(reverse = True)
print "List is sorted by descending order: ", l6
print "-" * 145

# The reverse() method reverses the elements of a given list.
print 'The list is : ["Apple", "Ball", "Catch", "DRS", "Eat", "Food"]'
reverse_list = l8.reverse()
print "The reversed list is: ", l8
print "-" * 145

"""# The copy() method returns a shallow copy of the list.
print "-" * 145
copy_list = l2.copy()
print "Showing list is copycat of list l1", copy_list
print "-" * 145"""
