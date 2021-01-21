# Create a dictionary containing personal information:

name = input('What is your name?\n')
gender = input('What is your gender?\n')
profile = dict(name = name.title(), age = 16 , gender = gender.title())
print(profile)

# Definition and Usage
# The dict() function creates a dictionary.
# A dictionary is a collection which is unordered, changeable and unindexed.

# Syntax
# dict(keyword arguments)

# parameter	        Description

# keyword arguments	Required. As many keyword arguments you like, separated by comma: 
#                     key = value, key = value ...

even_numbers = [number for number in range(0,11) if number % 2 == 0]
expected_numbers = ['zero','two', 'four', 'six', 'eight']

result = dict(zip(expected_numbers, even_numbers))
print(result)
