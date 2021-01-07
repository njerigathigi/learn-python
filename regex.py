# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

# import re 

# When you have imported the re module, you can start using regular expressions:

# Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = 'The rain in Spain'
x = re.search('^The.*Spain$', txt) 
if x :
    print('match found!')
else:
    print('no match')
 
print()
# # ^ - starts with , $ - endswith * ,  . - Any character 
# (except newline character)
#string starts with the followed by  one or more occurrence of any other character except
#newline and ends with the word Spain

# if x :
#     print('match found!')
# else:
#     print('no match')

# RegEx Functions

# The re module offers a set of functions that allows us to search a string for a match:

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string

txt = 'Hello world'
x = re.search('^H.*d$', txt)
print(x)
if x :
    print('match found')
else:
    print('no match')

print()

# Metacharacters
# Metacharacters are characters with a special meaning:

# Character	Description	         
# []	    A set of characters	"[a-m]"	
# \	        Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	        Any character (except newline character)	"he..o"	
# ^	        Starts with	"^hello"	
# $	        Ends with	"world$"	
# *	        Zero or more occurrences	"aix*"	
# +	        One or more occurrences	"aix+"	
# {}	    Exactly the specified number of occurrences	"al{2}"	
# |	        Either or	"falls|stays"	
# ()	    Capture and group

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below,
# and has a special meaning:	 

text = 'The rain in Spain falls mainly in the plain!'

startswith_and_endswith = re.findall('^The.*!$', text) #returns a list of the whole string
print(startswith_and_endswith)

if startswith_and_endswith:
    print('match found!')
else:
    print('no match.')

print()

contains_a_to_r = re.findall('[a-r]', txt) #any letters between a and r
print(contains_a_to_r)

if contains_a_to_r:
    print('match found!')
else:
    print('no match')

print()

one_or_more_occurrences_of_char = re.findall('aix+', text)
print(one_or_more_occurrences_of_char)

if one_or_more_occurrences_of_char:
    print('match found!')
else:
    print('no match')

print()

specified_no_of_occurrences = re.findall('al{2}', text) #if alll it truncates the last l and returns all
print(specified_no_of_occurrences)

if specified_no_of_occurrences:
    print('match found!')
else:
    print('no match')

print()

either_all = re.findall('falls|drops', text)
print(either_all)

if either_all:
    print('match found')
else:
    print('no match!')
