#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
# To create a class, use the keyword class:
# The __init__() is used to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:
# its always executed when the class is being initiated.
#The __init__() function is called automatically every time the 
# class is being used to create a new object.
#Objects can also contain methods. Methods in objects are functions 
# that belong to the object.
#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.
#It does not have to be named self , you can call it whatever you like, 
#but it has to be the first parameter of any function in the class:




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, new_age):
        self.age = new_age

fiona = Person('Njeri', 20)
print(fiona.name)
print(fiona.age)
fiona.set_age(26)
print(fiona.age)

# You can modify properties on objects like this:
fiona.age = 40
print(fiona.age)

# You can delete properties on objects by using the del keyword:

# del fiona.age
# print(fiona.age)

#You can delete objects by using the del keyword:

# del fiona

# print(fiona)


# class definitions cannot be empty, but if you for some reason 
# have a class definition with no content, put in the pass statement 
# to avoid getting an error.

class People:
    pass

