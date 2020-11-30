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
# You can add as many arguments as you want.just separate them with a 
# comma.  



# An argument is the value that is sent to the function when it is called.





def printName(fname, lastname):
    print('Your name is {0} {1}.'.format(fname, lastname))

printName('Fiona', 'Njeri')


# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function 
# with 2 arguments, not more, and not less.


# Arbitrary Arguments, *args

# Arbitrary Arguments are often shortened to *args in Python documentations

# If you do not know how many arguments that will be passed into your function,
#  add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, 
# and can access the items accordingly:


def myfunction(*kids):
    # print(kids)
    print(kids[2])

# myfunction('leila', 'peace', 'jack')

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_functionn(child3, child2, child1):
    print('The youngest child is {}'. format(child3))

my_functionn(child1 = 'Leila', child3 = 'Jack', child2 = 'Peace')

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
#help avoid passing the wrong positional argument

# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items 
# accordingly:




def this_function(**kids):
    print('my childs  name is {}  {}'.format(kids['fname'], kids['lastname']))

this_function(fname = 'Leila', lastname = 'Shiru')    

# Default Parameter Value
# If we call the function without argument, it uses the default value:

def newfunction(country = 'Kenya'):
    print('I am from {}.'.format(country))

newfunction()

# You can send any data types of argument to a function (string, number, list, 
# dictionary etc.), and it will be treated as the same data type inside the function.

def foods(food):
    for meal in food:
        print(meal)

foods(['banana', 'pilau', 'samosa', 'cake'])

# Return Values

# To let a function return a value, use the return statement:
#return is used  to exit a function and return a value

def multiplication(number):

        return 5 * number
print(multiplication(6))

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function 
# definition with no content, put in the pass statement to avoid getting an error.

# def myfunction():
#     pass

def tri_recussion(k):
    if (k > 0):
        result = k + tri_recussion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('\n\nRecursion example results')
tri_recussion(5)
