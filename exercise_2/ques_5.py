temperature = int(input("Enter the temperature:"))

if temperature > 30:
    print("It's hot! Wear sunglasses!")
elif temperature >= 15 and temperature <= 30:
    print("It's nice outside! Enjoy!")
else:
    print("It's cold! Wear a jacket!")
