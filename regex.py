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
    
print()

# Special Sequences


# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
#       (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
#       r"\bain" r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning 
#       (or at the end) of a word
#       (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
#       r"\Bain" r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters 
#       (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	

print()
text1 = 'The rain in Spain'
characters_at_beginning_of_str = re.findall('\AThe', text1) #case sensitive. will return empty
                                                            #list if 'the' in lowercase.

print(characters_at_beginning_of_str)

if characters_at_beginning_of_str:
    print('match found!')
else:
    print('no match')

print()
characters_at_beginning_of_str_or_end = re.findall(r'\bThe', text1) #r -rawstring .
characters_at_beginning_of_str_or_end2 = re.findall(r'ain\b',text1) #normally \b - bytes literal 

print(characters_at_beginning_of_str_or_end)
print(characters_at_beginning_of_str_or_end2)
print()


char_present_but_not_in_beg_or_end = re.findall(r'\Bain', text1)
char_present_but_not_in_beg_or_end2 = re.findall(r'ain\B', text1)
print(char_present_but_not_in_beg_or_end)
print(char_present_but_not_in_beg_or_end2)
print()


str_contains_digits = re.findall('\d', text1)
print(str_contains_digits)
print()

str_with_no_digits = re.findall('\D', text1) #returns match at each character thats not a digit.
print(str_with_no_digits) #list with every non-digit character as item
print()

str_with_whitespace = re.findall('\s', text1)
print(str_with_whitespace) #list with every whitespace character as item
print()

str_without_whitespace = re.findall('\S', text1)
print(str_without_whitespace) #list with every non-whitespace character as item.
print()

text2 = 'Nala_cat....,,,,,,,, was my 1.0 st furbaby'

str_with_word_characters = re.findall('\w', text2)
print(str_with_word_characters) #all letters, numbers and underscore. if floating point , (.) , is ignored.
print()

str_without_word_character = re.findall('\W', text2)
print(str_without_word_character)
print()

characters_at_end_of_str = re.findall('ain\Z', text1)
print(characters_at_end_of_str)
