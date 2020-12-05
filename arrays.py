# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# This shows how to use LISTS as ARRAYS.

# Arrays are used to store multiple values in one single variable:

cars = ['Ford', 'Volvo', 'BMW', 'BMW']
print(cars.count('BMW'))

# What is an Array?

# An array is a special variable, which can hold more than one value at a time.
# An array can hold many values under a single name, and you can access the values 
# by referring to an index number.

# Access the Elements of an Array
# You refer to an array element by referring to the index number.

first_car = cars[0]
print(first_car)

# Modify the value of the first array item:

cars[0] = 'Toyota'
print(cars[0])

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).

print(len(cars))
# The length of an array is always one more than the highest array index.

# You can use the for in loop to loop through all the elements of an array.

for car in cars:
    print(car)

# Adding Array Elements

cars.pop(1)
print(cars)


# You can use the append() method to add an element to an array.

cars.append('Ford')
print(cars)
cars.extend(['subaru', 'vitz'])
print(cars)

# Removing Array Elements

# you can use the pop() method to remove an element from the array

# Delete the second element of the cars array

cars.pop(1)
print(cars)

# You can also use the remove() method to remove an element from the array

cars.remove('subaru')
print(cars)

cars.insert(2, 'nissan')
print(cars)
# syntax
# list.insert(pos, elmnt)


# The list's remove() method only removes the first occurrence of the specified value.

# Array Methods               Method	Description
# append()	                Adds an element at the end of the list
# clear()	                    Removes all the elements from the list
# copy()	                    Returns a copy of the list
# count()	                    Returns the number of elements with the specified value
# extend()	                Add the elements of a list (or any iterable), to the end of the current list
# index()	                    Returns the index of the first element with the specified value
# insert()	                Adds an element at the specified position
# pop()	                    Removes the element at the specified position
# remove()	                Removes the first item with the specified value
# reverse()	                Reverses the order of the list
# sort()	                    Sorts the list
