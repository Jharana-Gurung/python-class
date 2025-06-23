# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:

    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:

    print("You can't divide by zero!")

except ValueError:
    print("Please enter only numbers.")


# Write a Python program that prompts the user to input an integer and raises a ValueError
# exception if the input is not a valid integer.
try:

    user_input = input("Enter an integer: ")

    number = int(user_input)

    print("You entered:", number)

except ValueError:

    print("That's not a valid integer!")

# Write a Python program that prompts the user to input two numbers and raises a TypeError
# exception if the inputs are not numerical.
try:

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numbers.")

    num1 = float(num1)
    num2 = float(num2)

    print("Sum:", num1 + num2)

except TypeError as te:
    print("TypeError:", te)
