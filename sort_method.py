# The sort() method sorts the list ascending by default.
# The sort() method sorts the list ascending by default.

#syntax
# list.sort(reverse=True|False, key=myFunc)

# Parameter	         Description
# reverse	       Optional. reverse=True will sort the list descending. Default is reverse=False
# key	           Optional. A function to specify the sorting criteria(s)

cars = ['Ford', 'BMW','ea','Volvo']
cars.sort()
print(cars)
print()
cars.sort(reverse = True)
print(cars)
print()

# Sort the list by the length of the values:

def length(data):
    return len(data)

cars.sort(key= length)
print(cars)

print()

cars.sort(key= lambda x : x[1])
print(cars)

#each item in the iterable is passed into the function individually 

# Sort a list of dictionaries based on the "year" value of the dictionaries:

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def year(data):
    return data['year']

cars.sort(key=year)
print(cars)
print()

# Sort the list by the length of the values and reversed:

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def length_of_cars(car):
    return len(car)

cars.sort(reverse= True, key= length_of_cars)
print(cars)
