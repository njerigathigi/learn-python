# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# In Python a function is defined using the def keyword:

def my_function():
    print('Hello from a function.')

# To call a function, use the function name followed by parenthesis:

my_function()

# parameter and argument can be used for the same thing: information that are passed 
# into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.


def printName(fname, lastname):
    print('Your name is {0} {1}.'.format(fname, lastname))

printName('Fiona', 'Njeri')


# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function 
# with 2 arguments, not more, and not less.

