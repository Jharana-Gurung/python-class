def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return None


sum = calculator(1, "+", 2)


def sum_of_n_numbers():
    num = int(input("Enter a number: "))
    total = 0
    for i in range(1, num + 1):
        total = total + i
    print(f"The sum is {total}")


sum_of_n_numbers()


def area(r, pi=4):
    a = pi * r ** 2
    return a


print(area(5))

# class Student:
#     college = "ICP"
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         return f"mero naam {self.name} ho and ma {self.college} ma padchu."

# student1 = Student("Ram")
# student2 = Student("Sita")

# print(student1.introduce())
