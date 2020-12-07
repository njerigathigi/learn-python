# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

nala = '''i love my cat
Nala.She is late but i
miss her everyday.May 
she rest in peace.'''

print(nala)
# in the result, the line breaks are inserted at the same position as in the code.


# To check if a certain phrase or character is present in a string, we can use the keyword in.

print('Nala' in nala)

if 'Nala' in nala : 
    print('I love you {}!'.format('Nala')) 
else:
    print('Nala not in sentence')

# To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword not in.

print('dog' not in nala)

# Slice From the Start

hello = 'hello, world!'
print(hello[:5])

# By leaving out the end index, the range will go to the end:

print(hello[:])

# Use negative indexes to start the slice from the end of the string:
print(hello[-5:-1])

#backwards
print(hello[::-1])

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often 
# you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end
#returns a new string.The original string remains unchanged.

greeting = ' Hello, world! '
print(greeting.strip())
print(greeting)

# Replace String
# The replace() method replaces a string with another string:
#returns a new string
print(greeting.replace('H', 'J'))
print(greeting)


# Split String
# The split() method returns a list where the text between the specified separator 
# becomes the list items
# The split() method splits the string into substrings if it finds instances of the separator:

print(greeting.split(','))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator

# The format() method takes unlimited number of arguments, and are placed into 
# the respective placeholders


# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# \'	Single Quote	
# \\	Backslash	
# \n	New Line
# \t	Tab	
# \b	Backspace

# String Methods
# All string methods returns new values. They do not change the original string.


# Method	          Description
# capitalize()	Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	    Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning
