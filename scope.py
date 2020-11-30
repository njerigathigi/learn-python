# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.

def myfunction():
    x = 300
    print(x)

myfunction()

# in the example above, the variable x is not available outside the function, but it is
#  available for any function inside the function:

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope

# A variable created in the main body of the Python code is a global variable and
#  belongs to the global scope.
# Global variables are available from within any scope, global and local.

x = 300

def myfuncc():
    print(x)

myfuncc()
print(x)

# Naming Variables

# if you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables
# one available in the global scope (outside the function) and one available in the 
# local scope (inside the function):

y = 200

def myffunc():
    y = 200
    print(y)

print(y)
myffunc()

# The function will print the global y, and then the code will print the local y.

# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, 
# you can use the global keyword.
# The global keyword makes the variable global.
# If you use the global keyword, the variable belongs to the global scope:

def myfunncc():
    global z
    z = 500

myfunncc()
print(z)

# Also, use the global keyword if you want to make a change to a global variable inside 
# a function.


w  = 700

def myyfunc():
    global w
    w = 600

myyfunc()
print(w)
