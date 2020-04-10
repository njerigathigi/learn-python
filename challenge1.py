#write a function that accepts one argument.
#argument must be an integer
#if argument is divisible by 5 it should print "foo"
#if argument is divisible by 3 ,print "Bah"
#if its divisble by both 3 and 5, print"Foo Bah"

def division_test(number):
    value = int(number)
    if value % 3 == 0 and value % 5 == 0:
        print("Foo Bah")
        
    elif value % 3 == 0:
        print("Bah")
    
    elif value % 5 == 0:
        print("Foo ")

division_test(30005)
