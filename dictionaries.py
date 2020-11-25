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
