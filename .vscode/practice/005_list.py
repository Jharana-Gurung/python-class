# Write a Python program to multiply all the items in a list.
numbers = [2, 3, 4]

result = 1

for num in numbers:
    result = result * num

print("The multiplication of all numbers is:", result)


# Write a Python program to get the largest number from a list.
numbers = [5, 10, 3, 8, 2]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num  
print("The largest number is:", largest)

# Write a Python program to get the smallest number from a list.
numbers = [5, 10, 3, 8, 2]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num  

print("The smallest number is:", smallest)
