try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print(f"The result is : {result}")
except Exception:
    print("Invalid Input!")
finally:
    print("Thank you for using it.")
