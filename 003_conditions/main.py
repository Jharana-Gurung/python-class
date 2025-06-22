user_age = int(input("Enter your age"))
if user_age > 18:
    print("You are a voter")
else:
    print("You are not a voter")


num = int(input("Enter a number: "))
if num == 0:
    print("It is zero")
elif num % 2 == 0:
    print("It is even")
else:
    print("It is odd")


num = int(input("Enter a number: "))
if num % 7 == 0 and num % 5 == 0:
    print("divisible by 7 and 5")
elif num % 7 == 0:
    print("divisible by 7")
elif num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5 and 7")


num1 = int(input("Enter the first number:"))
operator = input("Enter the operator")
num2 = int(input("Enter the second number:"))

if operator == "+":
    operation = num1 + num2
    print(f" The sum of {num1} and {num2} is {operation}.")
elif operator == "-":
    operation = num1 - num2
    print(f"The subtraction of {num1} and {num2} is {operation}.")
elif operator == "*":
    operation = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {operation}.")


lucky_number = 10
user_guess = 0
while user_guess != lucky_number:
    user_guess = int(input("Guess the lucky number:"))
    if user_guess == lucky_number:
        print("Well guessed.")
    else:
        print("Try again.")

# another way
while True:
    num = int(input("Guess the number:"))

    if num == 5:
        print("Well Guessed.")
        break
    else:
        print("Try again.")


fruits = ["apple", "banana", "mango", "grapes", "kiwi"]
favourite_fruit = input("Enter your first favourite fruit:")
for favourite_fruit in fruits:
    if favourite_fruit != fruits:
        fruits.append(favourite_fruit)
    else:
        print("The fruit exist already.")
