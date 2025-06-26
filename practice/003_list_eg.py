numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

find_even_odd = {}

for num in numbers:
    if num % 2 == 0:
        find_even_odd[num] = "Even"
    else:
        find_even_odd[num] = "Odd"

print(find_even_odd)
