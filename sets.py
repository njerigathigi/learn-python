myset = {'apple', 'banana', 'cherry'}

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections 
# of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is both unordered and unindexed.
# you cannot be sure in which order the items will appear.

# Sets are written with curly brackets.

print(myset)
print()

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and 
# cannot be referred to by index or key.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.
# Sets cannot have two items with the same value.

# Duplicate values will be ignored:

fruits = {'apple', 'banana', 'cherry', 'apple'}
print(fruits)
print()

# To determine how many items a set has, use the len() method.

print(len(fruits))
print()

# Set items can be of any data type:

set1 = {'apple', 'banana', 'cherry'} #str
set2 = {1, 2, 3, 4, 5} #int
set3 = {True, False, True, False} #bool

# A set can contain different data types:

set4 = {1, 'apple', True, 3.0}

# type()
# sets are defined as objects with the data type 'set':

# The set() Constructor

# It is also possible to use the set() constructor to make a set.

thisset = set(('apple', 'banana', 'cherry'))
print(thisset)
print()

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for item in thisset:
    print(item)
    
print('banana' in thisset)
print()

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.

thisset.add('orange')
print(thisset)
print()

# To add items from another set into the current set, use the update() method.
fruits1 = thisset
tropical = {'pineapple', 'mango', 'papaya'}

fruits1.update(tropical)
print(fruits1)

# The object in the update() method does not have be a set, it can be any iterable 
# object (tuples, lists, dictionaries et,).

mylist = ['kiwi', 'grapes']
fruits1.update(mylist)
print(fruits1)

# Python - Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
# if the item to remove does not exist, remove() will raise an error.
# if the item to remove does not exist, discard() will NOT raise an error.

fruits1.remove('kiwi')
print(fruits1)
print('kiwi' in fruits1)
print()

fruits1.discard('papaya')
print(fruits1)
print('papaya' in fruits1)
print()

# You can also use the pop(), method to remove an item, but this method will remove
# the last item. Remember that sets are unordered, so you will not know what item that 
# gets removed.
# The return value of the pop() method is the removed item.
# Sets are unordered, so when using the pop() method, you do not know which item 
# that gets removed.

print(fruits1.pop())
print(fruits1)
print()
removed_fruit = fruits1.pop()
print(removed_fruit)
print(fruits1)
print()

# The clear() method empties the set:

newset = {'banana', 'mango', 'orange'}
# newset.clear()
# print(newset)
print()

# The del keyword will delete the set completely:

# del newset
# print(newset)

# Loop Items
# You can loop through the set items by using a for loop:

for fruit in newset:
    print(fruit)
print()
 # There are several ways to join two or more sets in Python. 

# You can use the union() method that returns a new set containing all items from both
# or the update() method that inserts all the items from one set into another:

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:

set4 = {9, 10, 11, 12}
set5 = {'a', 'b', 'c', 'd'}

set4.update(set5)
print(set4)
# Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are 
# present in both sets.

u = {'banana', 'apple', 'kiwi', 'papaya', 'orange'}
t = {'pineapple', 'apple', 'orange', 'mango'}

u.intersection_update(t)
print(u)

# The intersection() method will return a new set, that only 
# contains the items that are present in both sets.

z = u.intersection(t)
print(z)


# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements 
# that are NOT present in both sets.

u.symmetric_difference_update(t)
print(u)

# The symmetric_difference() method will return a new set, that contains only the 
# elements that are NOT present in both sets.

w  = u.symmetric_difference(t)
print(w)

# Method	                Description

# add()	              Adds an element to the set
# clear()	              Removes all the elements from the set
# copy()	              Returns a copy of the set
# difference()          Returns a set containing the difference between two or more sets
# difference_update()	  Removes the items in this set that are also included in another, specified set
# discard()	          Remove the specified item
# intersection()	      Returns a set, that is the intersection of two other sets
# intersection_update()   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	      Returns whether two sets have a intersection or not
# issubset()	          Returns whether another set contains this set or not
# issuperset()	      Returns whether this set contains another set or not
# pop()	              Removes an element from the set
# remove()	          Removes the specified element
# symmetric_difference()	           Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	   inserts the symmetric differences from this set and another
# union()	                           Return a set containing the union of sets
# update()	                       Update the set with the union of this set and others
