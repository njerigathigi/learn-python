# When you run a condition in an if statement, Python returns True or False:
a = 5
b= 10

if b > a:
    print('b is greater')
else:
    print('a is greater')

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# Some Values are False
# In fact, there are not many values that evaluates to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None.
#  And of course the value False evaluates to False.

# You can execute code based on the Boolean answer of a function:

def Myfunction():
    return True

if Myfunction():
    print('YES!')
else:
    print('NO!')


# Python also has many built-in functions that returns a boolean value, 
# like the isinstance() function, which can be used to determine if an object 
# is of a certain data type:

x = 200
print(isinstance(x, str))
