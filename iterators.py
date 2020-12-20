# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse 
# through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, 
# which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers
#  which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

fruits = ('apple', 'banana', 'cherry')
my_it = iter(fruits)


print(my_it)
print(my_it)
print(my_it)


print(next(my_it))
print(next(my_it))
print(next(my_it))

# Even strings are iterable objects, and can return an iterator

fruit = 'banana'

it = iter(fruit)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:

# for fruit in fruits:
#     print(fruit)
                     #try running both loops simultaneously
for character in fruit:
    print(character)

# The for loop actually creates an iterator object and executes the next() method 
# for each loop.


# Create an Iterator

class My_numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = My_numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self.a

    def __next__(self):
        x = self.a
        self.a += 1
        return x

print()

lst = [11, 22, 33, 44, 55]
iter_list = iter(lst)

while True:
    try:
        print(iter_list.next())
    except:
        break
