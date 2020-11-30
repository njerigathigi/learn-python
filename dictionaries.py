# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
#its unordered because its items do not have a defined order ie you cannot
#refer to an item by using an index.
# Dictionaries are changeable, meaning that we can change, add or 
# remove items after the dictionary has been created.
# To determine how many items a dictionary has, use the len() function
# The values in dictionary items can be of any data type:
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values

this_dict = {
    'brand': 'benz',
    'electric': False,
    'year' : 1964,
    'year' : 2020,
    'colours' : ['red', 'white', 'blue']
}

print(this_dict)

# You can access the items of a dictionary by referring to its key name, inside square brackets:

print(this_dict['brand'])


# There is also a method called get() that will give you the same result:
# The get() method returns the value of the item with the specified key.
# dictionary.get(keyname, value)
# keyname	Required. The keyname of the item you want to return the value from
# value	Optional. A value to return if the specified key does not exist.
# Default value None

print(this_dict.get('type', 'use brand'))

# Try to return the value of an item that do not exist:

print(this_dict.get('price', 20000))

# The keys() method will return a list of all the keys in the dictionary.

x = this_dict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to 
# the dictionary will be reflected in the keys list.

car = {
    'brand': 'ford',
    'electric': False,
    'year': 1964,
    'colours': ['red', 'white', 'blue'],
}

x = car.keys()
print(x)

car['price'] = 20000

x = car.keys()
print(x)
print(car)


# The values() method will return a list of all the values in the dictionary.
# No parameters
# The values() method returns a view object. The view object contains the 
# values of the dictionary, as a list.
# The list of the values is a view of the dictionary, meaning that any changes
# done to the dictionary will be reflected in the values list.

x = this_dict.values()
print(x)


# The items() method will return each item in a dictionary, as tuples in a list.
# The returned list is a view of the items of the dictionary, meaning that any changes 
# done to the dictionary will be reflected in the items list.

x =this_dict.items()
print(x)

# To determine if a specified key is present in a dictionary use the in keyword:

if 'brand' in this_dict:
    print(True)
else:
    print(False)


# You can change the value of a specific item by referring to its key name:

this_dict['brand'] = 'Mustang'
print(this_dict)


# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.




this_dict.update({'Assembled in' : 'Kenya'})
print(this_dict)
this_dict.update({'brand': 'Ford'}) # If the item does not exist, the item will be added.

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

this_dict['6 wheeler'] = False
print(this_dict)


# The pop() method removes the item with the specified key name:

this_dict.pop('6 wheeler')
print(this_dict)

# the popitem() method removes the last inserted item

this_dict.popitem()
print(this_dict)

# The del keyword removes the item with the specified key name:
del this_dict['brand']
print(this_dict)

# The del keyword can also delete the dictionary completely:

# del this_dict
print(this_dict)

# The clear() method empties the dictionary:

# this_dict.clear()
print(this_dict)

# You can loop through a dictionary by using a for loop
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

for x in this_dict:
    print(x)

# Print all values in the dictionary, one by one:

for x in this_dict:
    print(this_dict[x])

# Print all values in the dictionary, one by one:

for x in this_dict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in this_dict.keys():
    print(x)

# Loop through both keys and values, by using the items() method:

for x, y in this_dict.items():
    print(x , y)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only 
# be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

myDict = this_dict.copy()
print(myDict)

mydict = dict(this_dict)
print(mydict)


# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three dictionaries, then create one dictionary that will contain the other 
# three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for data in myfamily:
    print(data)
    for child , year in data.items():
        print(child)
        print(year)
        print()

# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
