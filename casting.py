# There may be times when you want to specify a type on to a variable.
# This can be done with casting.
#Python is an object-orientated language, and as such it uses 
# classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, 
# a float literal (by rounding down to the previous whole number), 
# or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal,
# a float literal or a string literal (providing the string represents 
# a float or an integer)
# str() - constructs a string from a wide variety of data types, 
# including strings, integer literals and float literals

a = int(1)
b = int(2.8) #2

c = float(2)
d = float('3') # 3.0
e = float('4.2') #4.2
f = str('s1') #'s1'
g = str(2) #'2'
h = str(3.0) #'3.0'
