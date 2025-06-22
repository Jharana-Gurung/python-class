fruits = ["banana", "apple"]
for fruit in fruits:
    print(fruit)


for i in range(0, 1000):
    print(f"{i + 1} Jharana Gurung")


i = 0
while i < 1000:
    i += 1
    if i == 5:
        continue
    print(f"{i} Jharana Gurung")
    if i == 99:
        break
