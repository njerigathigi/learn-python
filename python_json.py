# JSON is a syntax for storing and exchanging data
#data is sent in the form of a string.
#the object itself would be too big to send thus the need for conversion
#into a string.
# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work 
# with JSON data.

# Import the json module:

import json
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
profile = '{ "name": "John", "age":30, "city": "New York" }'

# parse x:
new_profile = json.loads(profile)
print(new_profile)
# the result is a Python dictionary:
print(new_profile['age'])
print()
print()
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using 
# the json.dumps() method.

# Convert from Python to JSON:

employee = {
    "name": "John",
    "age" : 30,
    "city": "New York",
}

# convert into JSON:
employee_json = json.dumps(employee)
# the result is a JSON string:
print(employee_json)
print()
print()

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# When you convert from Python to JSON, Python objects are converted into the 
# JSON (JavaScript) equivalent:

# Python	JSON
# dict	    Object
# list	    Array
# tuple  	Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

profile1 = {
    "name": "John",
    "age" : 30,
    "city": "New York",
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1},
    ]
}

print(json.dumps(profile1))
print()
print()

# Format the Result
# The example above prints a JSON string, but it is not very easy to read,
# with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:

# Use the indent parameter to define the numbers of indents
print(json.dumps(profile1, indent = 4))
print()
print()

# you can also define the separators, default value is (", ", ": "), 
# which means using a comma and a space to separate each object, and a 
# colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:
print(json.dumps(profile1, indent = 4, separators = (". ", "= ")))
print()
print()

# Order the Result
# Use the sort_keys parameter to specify if the result should be sorted or not:

print(json.dumps(profile1, indent = 4, separators = (". ", "= "), sort_keys = True))
