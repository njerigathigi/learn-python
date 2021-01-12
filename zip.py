# Join two tuples together:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

print(list(zip(a,b)))
print()

# The zip() function returns a zip object, which is an iterator of tuples where the 
# first item in each passed iterator is paired together, and then the second item in 
# each passed iterator are paired together etc.

# If the passed iterators have different lengths, the iterator with the least 
# items decides the length of the new iterator.

# Syntax

# zip(iterator1, iterator2, iterator3 ...)

# Parameter	                              Description
# iterator1, iterator2, iterator3 ...	  Iterator objects that will be joined together

# If one tuple contains more items, these items are ignored:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

print(frozenset(zip(a,b)))
