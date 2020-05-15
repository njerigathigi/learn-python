#create a function that receives a list of integers
#as an argument and returns the sum of those integers.

numbers = [1,2,3,4,5]

def add(values):
    answer = 0

    for number in values:
        answer += number
    
    return answer

print("The sum is {}.".format(add(numbers)))
        