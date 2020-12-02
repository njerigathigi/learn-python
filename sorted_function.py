# The sorted() function returns a sorted list of the specified iterable object.

# You can specify ascending or descending order. Strings are sorted 
# alphabetically, and numbers are sorted numerically.
# You cannot sort a list that contains BOTH string values AND numeric values.

# sorted(iterable, key=func, reverse=True/False)

# Parameter	       Description

# iterable	  Required.  The sequence to sort, list, dictionary, tuple etc.
# key	      Optional.  A Function to execute to decide the order. Default is None.    #defaut values functions
# reverse	  Optional.  A Boolean. False will sort ascending, True will sort descending.   #default values functions
#                        Default is False


# Sort numeric:

a = (1, 11, 2)
x = sorted(a) #a is a tuple.its immutable thus the reassignment to x
print(x)

# Sort ascending:

a = ("h", "b", "a", "c", "f", "d", "e", "g")
y = sorted(a)
print(y)

# Sort descending:

z = sorted(a, reverse = True)
print(z)
