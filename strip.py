# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) 
# characters (space is the default leading character to remove)

# Syntax
# string.strip(characters)

# Parameter	Description
# characters	Optional. A set of characters to remove as leading/trailing characters

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
