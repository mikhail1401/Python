# Task 1. Write fucntion to reverse a given string
print("Task 1. Write function to revrse a give string")

def stringReverse(input_string):
    # reversed_string = input_string[::-1]
    reversed_string = ''.join(reversed(input_string))
    return reversed_string

print(stringReverse('abcd'))


# Task 2. Find the duplicate
print("\nTask 2. Find the duplicate")

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


# Task 3. Two Sum: Given an array of integers and a target value, 
# find two numbers in the array that add up to the target value.
print("\nTask 3. Two Sum: Given an array of integers and a target value, \
find two numbers in the array that add up to the target value.")

def two_sum(input_list, target):
    for a in input_list:
        for b in input_list:
            if a!=b and a+b == target:
                return a, b
        else:
            return "There are no such numbers"

array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
print(two_sum(array2, target))


# Task 4. Longest Substring Without Repeating Characters: 
# Find the length of the longest substring without repeating characters.
print("\nTask 4. Longest Substring Without Repeating Characters.")

def longest_substring(string):
    return None
    
