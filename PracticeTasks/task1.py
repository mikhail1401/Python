# Task 1. Write fucntion to reverse a given string
def stringReverse(input_string):
    # reversed_string = input_string[::-1]
    reversed_string = ''.join(reversed(input_string))
    return reversed_string

print(stringReverse('abcd'))
    
# Task 2. Find the duplicate
def duplicate(input_list):
    duplicate_exists = False
    duplicate_values = {}

    index = 0
    for number in input_list:
        if number not in duplicate_values:
            duplicate_values[number] = [index];
        else:
            duplicate_values[number].append(index)
            duplicate_exists = True
        index += 1 
    
    if duplicate_exists:
        result = {key : value for key, value in duplicate_values.items() if len(value) > 1}
        return result
    else:
        return "There are no duplicates in the provided list"
    
array = [3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 11]
print(duplicate(array))



