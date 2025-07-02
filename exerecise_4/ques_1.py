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
