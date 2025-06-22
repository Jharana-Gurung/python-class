# Write a Python program that calculates the area of a circle based on the radius entered by the user.

def area_of_circle(r, pi=3.14):
    area = pi * r ** 2
    return area


r = int(input("Enter the radius:"))

area = area_of_circle(r)

print(f"The area of the circle is {area}")

# Write a Python program to display the first and last colors from the following list.

color_list = ["Red", "Green", "White", "Black"]

first_color = color_list[0]
last_color = color_list[-1]

print("First color:", first_color)
print("Last color:", last_color)


# Write a Python program that determines whether a given number
# (accepted from the user) is even or odd, and prints an appropriate message to the user.

num = int(input("Enter a number:"))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
