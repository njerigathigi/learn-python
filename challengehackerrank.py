#write a function to determine whether a year is a leap year or not.

def is_leap(year):
    leap = False
    import re
    
    # Write your logic here
    if re.findall('00\Z', str(year)) and year % 400 == 0:
        leap = True
    elif re.findall('0{2}', str(year)) == [] and year % 4 == 0:
        leap = True
    
    return leap

print(is_leap(2021))
