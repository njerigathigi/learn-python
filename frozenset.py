# Freeze the list, and make it unchangeable:

mylist = ['cow', 'sheep', 'goat', 'chicken']

x =  frozenset(mylist)
print(x)

# Definition and Usage

# The frozenset() function returns an unchangeable frozenset object (which is like a 
# set object, only unchangeable).

# Syntax

# frozenset(iterable)

# Parameter Values

# Parameter	      Description
# iterable	      An iterable object, like list, set, tuple etc.


# Try to change the value of a frozenset item.

# This will cause an error:

# x[1] = 'elephant'
# print(x)
