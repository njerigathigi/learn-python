# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.

# Syntax

# string.split(separator, maxsplit)

# When maxsplit is specified, the list will contain the specified number of elements plus one.

# Parameter   Values
# Parameter	  Description
# 
# separator	  Optional. Specifies the separator to use when splitting the string. 
#             By default any whitespace is a separator
# maxsplit	  Optional. Specifies how many splits to do. Default value is -1, 
#             which is "all occurrences"

txt = "Welcome to earth"
x = txt.split()
print(x)

greetings = 'Hello Njeri! welcome , to, earth'
y = greetings.split(',')
print(y)

fruits = 'apple#banana#pineapple#cherry'
z = fruits.split('#')
print(z)

# Split the string into a list with max 2 items:

w = fruits.split('#', 1)
print(w)
# setting the maxsplit parameter to 1, will return a list with 2 elements!

m = fruits.split('#', 0)
print(m) #does not split.returns a list with the string as the only item

n = fruits.split('#', -1)
print(n) #splits at all occurences
