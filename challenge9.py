#create a function, format_input , that accepts any string and returns all
#numerics in it. Example : 
                 #calling 
                 #format_input('abc123')
                 #returns '123' as a string
#if input is empty, then return an empty string.


def Format_input(String):
    num = ''
    
    if String.isnumeric() == True:
        print(String)
    
    elif String == '':
        print('')
    
    elif String.isalnum() == True:
        
        for char in String:
            
            if char.isnumeric() == True:
                num +=char
        
        print(num)

Format_input('12adsn934')
