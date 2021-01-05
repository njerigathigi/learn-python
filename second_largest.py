numbers = [2, 3, 6, 6, 5]

def second_largest(nums):
    unique_numbers = list(set(nums))
    unique_numbers.sort(reverse = True)
    return unique_numbers[1]
    
print(second_largest(numbers))
