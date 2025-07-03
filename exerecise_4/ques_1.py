"""
FizzBuzz with a Twist (Loops and Conditionals)
Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz";
for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz". Additionally,
if the number is even, append "Even" to the output (e.g., 15 should print "FizzBuzzEven").
 Use loops and conditionals to implement this.

"""

for num in range(1, 51):
    output = ""
    if num % 3 == 0 and num % 5 == 0:
        output = "FizzBuzz"
    elif num % 3 == 0:
        output = "Fizz"
    elif num % 5 == 0:
        output = "Buzz"
    else:
        output = str(num)

    if num % 2 == 0:
        output += "Even"

    print(output)
