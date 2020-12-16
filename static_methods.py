# Static methods, much like class methods, are methods that are bound 
# to a class rather than its object.
# They do not require a class instance creation. So, they are not 
# dependent on the state of the object.
# creating a static method

# you can use the @staticmethod decorator.
# The syntax of @staticmethod is:
# @staticmethod
# def func(args, ...)

# differences between a static method and a class method 
# Static method knows nothing about the class and just deals
# with the parameters.
# Class method works with the class since its parameter is always 
# the class itself.


# When do you use static methods?
# 1. Grouping utility function to a class
# class Dates:
#     def __init__(self, date):
#         self.date = date
    
#     def get_date(self):
#         return self.date

#     @staticmethod
#     def to_dash_date(date):
#         return date.replace('/', '-')
        # The replace() method replaces a specified phrase with another 
        # specified phrase.
        # All occurrences of the specified phrase will be replaced, if nothing
        # else is specified.
        # string.replace(oldvalue, newvalue, count)
        # oldvalue	Required. The string to search for
        # newvalue	Required. The string to replace the old value with
        # count	Optional. A number specifying how many occurrences of the 
        # old value you want to replace. Default is all occurrences

# We can also create to_dash_date outside the class, but since it works only 
# for dates, it's logical to keep it inside the Dates class.

# date = Dates('16-12-2020')
# date_from_DB = '16/12/2020'
# date_with_dash = Dates.to_dash_date(date_from_DB)
# print(date_with_dash)

# if (date.get_date() == date_with_dash):
#     print('equal')
# else:
#     print('not equal')


# 2. Having a single implementation

class Dates:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        return date.replace('/', '-')
    
class Dates_with_slashes(Dates):
    def get_date(self):
        return Dates.to_dash_date(self.date)

date = Dates('16-12-2020')
date_from_DB = Dates_with_slashes('16/12/2020')

if date.get_date() == date_from_DB.get_date():
    print('equal')
else:
    print('not equal')


# Here, we wouldn't want the subclass Dates_with_slashes to override the static
# utility method to_dash_date because it only has a single use, i.e. change date
# to dash-dates.

# We could easily use the static method to our advantage by overriding 
# get_date() method in the subclass so that it works well with the 
# Dates_with_slashes class.
