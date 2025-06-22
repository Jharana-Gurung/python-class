# Write a Python program to find the median among three given numbers.
first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
third_number = int(input("Enter the third number:"))

numbers = [first_number, second_number, third_number]
numbers.sort()

median = numbers[1]

print("The median is:", median)


# # Write a Python program to make combinations of 3 digits.

for x in range(5):
    for y in range(5):
        for z in range(5):
            if x != y and y != z and x != z:
                print(x, y, z)


# Write a Python program that removes and prints every third number from a list
# of numbers until the list is empty
numbers = list(range(1, 11))
index = 0

while numbers:
    index = (index + 2) % len(numbers)
    print("Removed:", numbers.pop(index))
