# list


# Create a list of numbers from 1 to 10.
myList = list(range(1,11))
print(myList)

# Add the number 11 to the list using append.
myList.append(11)
print(myList)
# Insert the number 0 at the beginning of the list.
myList.insert(0,0)
print(myList)
# Remove the number 5 from the list using remove.
myList.remove(5)
print(myList)
# Find the index of the number 7 in the list.
myIndex = myList.index(7)
print("The index is", myIndex)
# Count how many times the number 3 appears in the list.
Counting = myList.count(3)
print(Counting)
# Sort the list in descending order.
myList.sort(reverse=True)
print(myList)
# Reverse the list.
myList.reverse
print(myList)
# Create a new list by copying the current list and add the number 100 to it.
# copied_list = myList.copy
# copied_list.append(100)
# # Clear all elements from the copied list.
# copied_list.clear()
#=================================================================

# Tuple


# Create a tuple with mixed data types and print its length.
myTuple = (1,"salam",True,False,328479.12)
print(len(myTuple))
# Count the number of times a specific value appears in a tuple.
myTuple = (1,2,3,4,5,2,3,4,1,4)
print(myTuple.count(2))
# Find the index of a specific value in a tuple.
print(myTuple.index(3))
# Convert a list to a tuple and sort it.
myList = [7,43,45,786,2]
myTuple = print(tuple(sorted(myList)))
# Unpack a tuple into individual variables.
k = (1,2,3)
a, b, c = k
print(a,b,c)
#========================================================================

# dictionary

# Create a dictionary of student names and grades. Add, update, and delete an entry.
students = {"Ali": 95, "Mehdi":80, "Kasra": 65}
students["Kamran"] = 75
print(students)
students["Ali"] = 88
print(students)
del students["Kasra"]
print(students)
# Write a function that counts the frequency of each character in a string using a dictionary.


# Merge two dictionaries.
a = {"a":1, "b":2}
b = {"c":3, "d":4}
merged = {**a, **b}
print(merged)
# Print all keys and values in a dictionary.


# Check if a key exists in a dictionary.

#=====================================================================

# Set

# Create a set from a list with duplicate values and print it.
duplicated_list = [1,2,3,4,5,6,7,8]
my_set = set(duplicated_list)
print(my_set)
# Find the union, intersection, and difference of two sets.
a = {1,2,3,4}
b = {5,6,7,8}
print("Union is" ,a|b)
print("Intersection is" ,a & b)
print("Difference is" ,a-b)
# Check if one set is a subset/superset of another.

# Add and remove elements from a set.
a.add(29)
print(a)
a.discard(2)
print(a)
# Find elements that are in one set but not both.

#========================================================================


# Frozenset

# Create a frozenset from a list.

# Find the intersection and difference between two frozensets.

# Check if an element is in a frozenset.

# Use a frozenset as a key in a dictionary.

# Compare a set and a frozenset for equality.