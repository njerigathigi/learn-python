# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py

# Use a Module
# we can use the module we just created, by using the import statement


# import mymodule as mx

# mymodule.greeting('Njeri')
# When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module
# The module can contain functions, as already described, but also variables of all 
# types (arrays, dictionaries, objects etc):

# print(mymodule.person1['name'])
# mymodule.greeting(mymodule.person1['name'])

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py
#.py indicates that its a python file

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword

# age = mx.person1['age']
# print(age)

#Built-in modules
#there are several built-in modules in Python, which you can import whenever you like.
 
# import platform

# x = platform.system()
# print(x)

# Using the dir() Function
#there is a built-in function to list all the function names(or variable names) in a module.
#The dir() function

# y = dir(platform)
# print(y)
#the dir() function can be used on all modules, also the ones you create yourself.

# Import From Module
# You can choose to import only parts from a module, by using the from keyword

from mymodule import person1

print(person1['age'])

# When importing using the from keyword, do not use the module name when referring to elements 
# in the module. Example: person1["age"], not mymodule.person1["age"]
