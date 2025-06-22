# Write a Python function to sum all the numbers in a list.
def sum_list(numbers):
    total = 0  
    for num in numbers:  
        total += num      
    return total  

my_numbers = [2, 4, 6, 8]

result = sum_list(my_numbers)
print("The sum is:", result)


# Write a Python function to multiply all the numbers in a list. 
def multiply_numbers(numbers):
    result = 1  
    for num in numbers:
        result *= num  
    return result

list = [2, 3, 4]
print("The result is:", multiply_numbers(list))


# Write a Python program to reverse a string.
user_input = input("Please enter a string: ")

reversed_string = ""

for char in user_input:
    reversed_string = char + reversed_string  

print("The reversed string is:", reversed_string)



