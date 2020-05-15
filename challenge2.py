#write a function that checks if a number is a prime number.

def isprime(value):
    number = int(value)
    
    if number == 2 or number == 3 :
        return True
        
    elif number % 3 == 0 or number % 5 == 0:
        return False
    
    elif number % 2 == 0 :
        return False
    
    else:
        return True

prime_number(19)
