# A date in Python is not a data type of its own, but we can import a module named 
# datetime to work with dates as date objects.


import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

# we have imported datetime module using import datetime statement.
# One of the classes defined in the datetime module is datetime class. 
# We then used now() method to create a datetime object containing the 
# current local date and time.

#  Get Current Date

date_object = datetime.date.today()
print(date_object)

# in this program, we have used today() method defined in the date class 
# to get a date object containing the current local date.

# What's inside datetime?

# We can use dir() function to get a list containing all attributes
# of a module

print(dir(datetime))


# Commonly used classes in the datetime module are:

# date Class
# time Class
# datetime Class
# timedelta Class


# datetime.date Class

# You can instantiate date objects from the date class. A date object
# represents a date (year, month and day).

d = datetime.date(2020, 12, 26)
print(d)

# date() in the above example is a constructor of the date class. 
# The constructor takes three arguments: year, month and day.

# We can only import date class from the datetime module. 

from datetime import date

current_date = date(2020, 12, 26)
print(current_date)

# Get current date

from datetime import date
today = date.today()
print(today)

# You can create a date object containing the current date by using a 
# classmethod named today()

# Get date from a timestamp

# We can also create date objects from a timestamp. A Unix timestamp is
# the number of seconds between a particular date and January 1, 1970 at UTC.
# You can convert a timestamp to date using fromtimestamp() method.

# why its always 1st jan 1970 , Because - '1st January 1970' usually 
# called as "epoch date" is the date when the time started for
# Unix computers, and that timestamp is marked as '0'. Any time
# since that date is calculated based on the number of seconds elapsed

from datetime import date
timestamp = date.fromtimestamp(3243546575)
print('Date =', timestamp)

# Print today's year, month and day

# We can get year, month, day, day of the week etc. from the date object easily

from datetime import date
today = date.today()
print('current year', today.year)
print('current month', today.month)
print('current day', today.day)
print()
print()

# datetime.time

# A time object instantiated from the time class represents the local time.

# Time object to represent time

from datetime import time
# time(hour = 0, minute = 0, second = 0)  default attributes
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56 )
print(b)

# time(hour, minute and second)
c = time(hour = 3, minute = 30, second = 10)
print(c)

#time(hour, minute, second, microsecond)\
d = time(hour = 5, minute = 45, second = 50, microsecond = 243566)
print(d)

# Print hour, minute, second and microsecond
from datetime import time
a = time(11, 12, 13)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
print()
print()
# Notice that we haven't passed microsecond argument. Hence, its default value 0 is printed.

#datetime.datetime
# the datetime module has a class named datetime that can contain information from both date 
# and time objects.

from datetime import datetime

# datetime(year, month, day)

w = datetime(2020, 12, 29)
print(w)

#datetime(year, month, day, hour, minute, second, microsecond)
n = datetime(2020, 12, 29, 12, 0, 0, 123445 )
print(n)
# The first three arguments year, month and day in the datetime() constructor are mandatory.

# Print year, month, hour, minute and timestamp
from datetime import datetime

m = datetime(2020, 12, 29, 12, 3, 50, 34567)
print('year:', m.year)
print('month:', m.month)
print('day:', m.day)
print('hour:', m.hour)
print('minute:', m.minute)
print('second:', m.second)
print('microsecond:', m.microsecond)
print('timestamp:', m.timestamp())
print()
print()

# datetime.timedelta
# A timedelta object represents the difference between two dates or times.

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  
# Notice, both t3 and t6 are of <class 'datetime.timedelta'> type

# Difference between two timedelta objects

from datetime import timedelta
z1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
z2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
z3 = z1 - z2

print("z3 =", z3)
# Here, we have created two timedelta objects t1 and t2, and their difference is printed on the screen.
# in the python datetime module, timedelta objects take weeks, days, hours, minutes, seconds,
# and microseconds as arguments upon instantiation. However, after the timedelta is created, 
# the only two attributes it has of the former listed are days, seconds, and microseconds.
