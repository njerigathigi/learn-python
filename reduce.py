# The reduce(fun,seq) function is used to apply a particular function passed in its argument 
# to all of the list elements mentioned in the sequence passed along.This function is defined 
# in “functools” module.

# Working : 

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

import functools
#initializing list
lis = [1, 2, 3, 4, 5, 6]

#using reduce to compute the sum of the list.
print("The sum of the list elements is : ", end = "")
print(functools.reduce(lambda a, b: a + b, lis))

#using reduce to compute maximum element from a list
print("The maximum item in the list is : ", end = "")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# Using Operator Functions
# reduce() can also be combined with operator functions to achieve the similar 
# functionality as with lambda functions and makes the code more readable.


import functools #for reduce
import operator  #for operator functions

numbers = [1, 2, 3, 4, 5, 6]

#sum

print('The sum of numbers is: ', end = '')
print(functools.reduce(operator.add, numbers))

#product

print('The product of numbers is: ', end = '')
print(functools.reduce(operator.mul, numbers))

#using reduce to concatenate string

print('THe concatenated product is: ', end = '')
print(functools.reduce(operator.add, ['fiona', 'FIFI', 'fiona']))
