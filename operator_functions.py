# Python has predefined functions for many mathematical, logical, relational, bitwise 
# etc operations under the module “operator”. Some of the basic functions are :


import operator


a = 4
b = 3

#add 
#add(a, b) :- This functions returns addition of the given arguments.
# Operation – a + b.

print('The addition of numbers is: ', end = '')
print(operator.add(a, b))

#sub
# sub(a, b) :- This functions returns difference of the given arguments.
# Operation – a – b.

print('The difference of numbers is: ', end = '')
print(operator.sub(a, b))

#mul
# mul(a, b) :- This functions returns product of the given arguments.
# Operation – a * b.

print('The product of numbers is: ', end = '')
print(operator.mul(a, b))

#truediv
# truediv(a,b) :- This functions returns division of the given arguments.
# Operation – a / b

print('The division of numbers is: ', end = '')
print(operator.truediv(a, b))

#floordiv
# floordiv(a,b) :- This functions also returns division of the given arguments. 
# But the value is floored value i.e. returns greatest small integer./truncated to the nearest 
# whole number.

print('The floored division of numbers is: ', end = '')
print(operator.floordiv(a , b))

#pow
# pow(a,b) :- This functions returns exponentiation of the given arguments.
# Operation – a ** b.

print('The exponentiation of numbers is: ', end = '')
print(operator.pow(a, b))

#mod
# mod(a,b) :- This functions returns modulus of the given arguments.
# Operation – a % b.

print('The modulus of numbers is: ', end = '')
print(operator.mod(a, b))

#lt
#  lt(a, b) :- This function is used to check if a is less than b or not. 
#  Returns true if a is less than b, else returns false.
# Operation – a < b.

print('a is less than b: ', end = '')
print(operator.lt(a , b))

#le
# This function is used to check if a is less than or equal to b or not. 
# Returns true if a is less than or equal to b, else returns false.
# Operation – a <= b.

print('a is less than or equal to b: ', end = '')
print(operator.le(a, b))

#eq
# eq(a, b) :- This function is used to check if a is equal to b or not. 
# Returns true if a is equal to b, else returns false.
# Operation – a == b.

print('a is equal to b: ', end = '')
print(operator.eq(a, b))

#gt
# gt(a,b) :- This function is used to check if a is greater than b or not. 
# Returns true if a is greater than b, else returns false.
# Operation – a > b.

print('a greater than b: ', end = '')
print(operator.gt(a, b))

#ge
# ge(a,b) :- This function is used to check if a is greater than or equal to b or not. 
# Returns true if a is greater than or equal to b, else returns false.
# Operation – a >= b.

print('a is greater than or equal to b: ', end = '')
print(operator.ge(a, b))

#ne
# ne(a,b) :- This function is used to check if a is not equal to b or is equal. 
# Returns true if a is not equal to b, else returns false.
# Operation – a != b.

print('a is not equal to be: ', end = '')
print(operator.ne(a, b))
