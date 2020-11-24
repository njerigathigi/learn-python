# List comprehension offers a shorter syntax when you want to create
#  a new list based on the values of an existing list.

# Based on a list of fruits, you want a new list, containing only 
# the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with 
# a conditional test inside:

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# new_fruitList = []

# for fruit in fruits:
#     if 'a' in fruit:
#         new_fruitList.append(fruit)

# print(new_fruitList)

# With list comprehension you can do all that with only one line of code:

new_fruitList = [fruit for fruit in fruits if 'a' in fruit]
print(new_fruitList)

#syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Only accept items that are not "apple":

not_apple = [fruit for fruit in fruits if fruit != 'apple']
print(not_apple)

# The condition is optional and can be omitted:

all_fruits = [fruit for fruit in fruits]
print(all_fruits)

# the iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)]
print(newlist)

#you can add a condition

newlist = [x for x in range(10) if x < 5]
print(newlist)


# the expression is the current item in the iteration, but it is also 
# the outcome, which you can manipulate before it ends up like a list 
# item in the new list.

fruits2 = [fruit.upper() for fruit in fruits]
print(fruits2)


# You can set the outcome to whatever you like:

fruits3 = ['hello' for fruit in fruits]
print(fruits3)

# The expression can also contain conditions, not like a filter, but as a 
# way to manipulate the outcome:

#Return 'orange' instead of 'banana'

fruits4 = [fruit if fruit != 'banana' else 'orange' for fruit in fruits]
print(fruits4)
