#Inheritance allows us to define a class that inherits all the methods 
#and properties from another class .
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
#Any class can be a parent class, so the syntax is the same as creating any other class:

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname, self.lastname)

# p1 = Person('Fiona', 'Njeri')
# p1.printname()

#To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:

# class Student(Person):
#     pass 
# Use the pass keyword when you do not want to add any 
# other properties or methods to the class.

# Now the Student class has the same properties and methods 
# as the Person class.

# x = Student('Fiona', 'Njeri')
# x.printname()


# When you add the __init__() function, the child 
# class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides 
# the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function,
#  add a call to the parent's __init__() function:

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name, self.last_name)


# class Student(Person):
#     def __init__(self, firstname , lastname):
#         Person.__init__(self, firstname, lastname)
#         self.graduationyear = 2021 #static

# Python also has a super() function that will make the child class 
# inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name 
# of the parent element, it will automatically inherit the methods 
# and properties from its parent.

# Add a method called welcome to the Student class:
# If you add a method in the child class with the same name 
# as a function in the parent class, the inheritance 
# of the parent method will be overridden.

class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def welcome(self):
        print(
            'Welcome {0} {1} to the class of {2}!'
            .format(self.first_name.title(), self.last_name.title(), 
            self.graduation_year)
            )


x = Student('fiona', 'Njeri', 2021)
x.printname()
print(x.graduation_year)
x.welcome()
