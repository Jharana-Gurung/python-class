lines = input("Enter the lines you want:")

words = lines.split(" ")

counter_dict = {}

for word in words:
    if word in counter_dict:
        frequency = counter_dict[word]
        counter_dict[word] = frequency + 1

    else:
        counter_dict[word] = 1

print(counter_dict)
