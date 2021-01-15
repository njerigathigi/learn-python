colors = ['red', 'orange', 'yellow', 'green']

# iterators are data types that can be used in a for loop. The most common iterator 
# in Python is the list.

#iterating list

for color in colors:
    print(color)

# Must import the itertools module before using. 

# accumulate()

# This iterator takes two arguments, iterable target and the function which would be 
# followed at each iteration of value in target. If no function is passed, addition takes 
# place by default. If the input iterable is empty, the output iterable will also be empty.

# Syntax

# itertools.accumulate(iterable, func)

# This function makes an iterator that returns the results of a function.


import itertools
import operator

numbers = [1, 2, 3, 4, 5]
numbers2 = [6, 5, 5, 7, 10, 9, 12, 11, 40]

result = itertools.accumulate(numbers, operator.mul)

print(result)

for each in result:
    print(each)

# use the max function 

maximum_number = itertools.accumulate(numbers2, max)
print(maximum_number)

for number in maximum_number:
    print(number)

# Note: The passing function is optional as if you will not pass any function items will be 
# summed i.e. added by default.


# itertools.accumulate(set.difference)

# This return accumulate of items of difference between sets.

nums = { 5, 3, 6, 2, 1, 9 } 
nums2 ={ 4, 2, 6, 0, 7 } 
  
result = itertools.accumulate(nums2.difference(nums))

print(result)

for number in result:
    print(number)

# Now this will first give difference  
# and the give result by adding all  
# the element in result as by default 
# if no function is passed it will add always
