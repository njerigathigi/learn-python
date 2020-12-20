# The map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.
# The map() function returns a map object(which is an iterator) of the results after 
# applying the given function to each item of a given iterable (list, tuple etc.)
# You can pass one or more iterable to the map() function.

# map(function, iterables)

# function	Required. The function to execute for each item
# iterable	Required. A sequence, collection or an iterator object. You can send as 
#                     many iterables as you like, just make sure the function has one 
#                     parameter for each iterable.

# Calculate the length of each word in the tuple

def length(item):
        return len(item)

fruits = ('banana', 'orange', 'passion', 'mangoes', 'tree tomato')

x = map(length, fruits)
print(x)
item_length_list= list(x)
print(item_length_list)

def addition(n):
    return n + n

numbers = (1, 2, 3, 4, 5)

doubled = map(addition, numbers)
print(doubled)
print(list(doubled))

# We can also use lambda expressions with map to achieve above result.

doubled = map(lambda x : x * 2, numbers)
print(doubled)
print(list(doubled))


# Add two lists using map and lambda 
  
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 

addition = map(lambda x, y: x + y, numbers1, numbers2)
print(addition)
print(tuple(addition))

l = ['sat', 'bat', 'cat', 'mat'] 

# map() can listify the list of strings individually 
new_list = map(list, l)
print(new_list)
print(list(new_list))
