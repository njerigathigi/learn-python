ages = [5, 12, 17, 18, 24, 32]

def adult(age):
    if age < 18:
        return False
    else:
        return True

adults = filter(adult, ages)
print(adults) #returns a filter object which is an iterator.

for age in adults:
    print(age)

# The filter() function returns an iterator were the items are filtered through a 
# function to test if the item is accepted or not.

# Syntax
# filter(function, iterable)

# Parameter	Description
# function	A Function to be run for each item in the iterable
# iterable	The iterable to be filtered
