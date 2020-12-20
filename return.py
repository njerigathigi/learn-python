def myfunc(x, y):
    return x + y

print(myfunc(2,2))

# The return keyword is to exit a function and return a value.
# Statements after the return line will not be executed:
# you can use a return statement only inside a function or method definition. 
# If you use it anywhere else, then you’ll get a SyntaxError:
# You can use any Python object as a return value including modules

def get_even(numbers):
    return [number for number in numbers if number % 2 == 0]

print(get_even([1, 2, 3, 4, 5, 6, 7, 8]))

# you can only use expressions in a return statement. Expressions are different 
# from statements like conditionals or loops.

def mean(sample):
    return sum(sample) // len(sample)

print(mean([1, 2]))

# A Python function will always have a return value.
# if you don’t explicitly use a return value in a return statement, or if you totally
# omit the return statement, then Python will implicitly return a default value for you. 
# That default return value will always be None.

def add_one(x):
    result = x + 1

print(add_one(5))

# You can use a return statement to return multiple values from a function. To do that, 
# you just need to supply several return values separated by commas.

import statistics as st #Python standard module statistics provides 
                        #several functions for calculating mathematical statistics of numeric data.

def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample) #returns a tuple
    #In Python, comma-separated values are considered tuples without parentheses , 
    # except where required by syntax

sample = [1, 1, 2, 3, 4, 5, 7, 7, 7]
mean , median, mode = describe(sample) #iterable unpacking #unpacking a tuple
print(mean, median, mode)

result = describe(sample) #tuple
print(result)
print(type(result))
