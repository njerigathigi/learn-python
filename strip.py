# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) 
# characters (space is the default leading character to remove)

# Syntax
# string.strip(characters)

# Parameter	Description
# characters	Optional. A set of characters to remove as leading/trailing characters

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
print()

#rstrip
# The rstrip() method removes any trailing characters 
# (characters at the end a string) ie on the right side of the string.
# space is the default trailing character to remove. 

#syntax
# string.rstrip(characters)

# Parameter	Description
# characters	Optional. A set of characters to remove as trailing characters

# y = txt.rstrip('rrr')
# print(y)

sentence = "banana,,,,,ssqqqww....."
fruit = sentence.rstrip(',sqw.')
print(fruit)

# lstrip
# The lstrip() method removes any leading characters ie to the left of the string
# space is the default leading character to remove

# Syntax
# string.lstrip(characters)

# Parameter	    Description
# characters	Optional. A set of characters to remove as leading characters

txt1 = ",,,,,ssaaww.....banana"
new_txt1 = txt1.lstrip(',saw.')
print(new_txt1)
