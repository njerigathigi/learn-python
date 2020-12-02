# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned

x = lambda a : a + 10
print(x(5))
 
# Lambda functions can take any number of arguments

y = lambda d, e : d * e
print(y(4, 5))

# Summarize argument a, b, and c and return the result

c = lambda a, b, c : a + b + c
print(c(1, 2, 3))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function 
# inside another function.
# Say you have a function definition that takes one argument, and that argument will
#  be multiplied with an unknown number

# def myfunc(n):
#     return lambda a: a * n

# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mytrippler = myfunc(3)
print(mytrippler(11))

# Use lambda functions when an anonymous function is required for a short period of time.
