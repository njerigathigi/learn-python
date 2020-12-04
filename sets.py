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
