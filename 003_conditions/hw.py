# Question no 1

age = int(input("Enter your age:"))

if age < 13:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior.")


# Question no 2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0 and num1 % num2 == 0:
    print("First number is divisible by second.")
else:
    print("First number is not divisible by second.")

# Question no 3

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even number and its square is:", number ** 2)
else:
    print("Odd number and its cube is:", number ** 3)
