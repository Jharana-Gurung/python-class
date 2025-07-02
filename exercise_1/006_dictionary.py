# Write a Python script to add a key to a dictionary.
my_dict = {
    "name": "Jharana",
    "age": 25
}
my_dict["city"] = "Pokhara"

print(my_dict)


# Write a Python program to iterate over dictionaries using for loops.
my_dict = {
    "name": "Jharana",
    "age": 25,
    "city": "Pokhara"
}

for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")


# Write a Python script to merge two Python dictionaries.
dict1 = {
    "name": "Jharana",
    "age": 25
}


dict2 = {
    "city": "Kathmandu",
    "country": "Nepal"
}

dict1.update(dict2)

print(dict1)
