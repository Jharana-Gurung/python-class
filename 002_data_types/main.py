
data = ("Swift Academy", 99998765432, True, ("Hello", 56.90))  # tuple
unique_data = {"Hello", 12, True, "World", "Hello"}  # set
student_data = {
    'name': "jharana gurung",
    'address': "lekhnath"
}  # dictionary

fruits = ["Apple", "Banana", "Carrot"]  # list
print(fruits[0])

print(unique_data)


snacks = ["Roti", "Chips", "Noodles", "Biscuits", {"Ram", "Shyam"}]
print(snacks[4][1])

personl_details = {
    "name": "Ram Gurung",
    "address": "Pokhara"
}
print(personl_details['address'])


data = [
    {
        "name": "Ram Gurung",
        "hobbies": ["Coding", [{
            "name": {
                "first": "Jharana"}
        }]]
    }
]
print(data[0]["hobbies"][1][0]['name']["first"])


fruits = ["apple", "banana", "mango", "grapes", "kiwi"]
favourite_fruit = input("Enter your first favourite fruit:")
for favourite_fruit in fruits:
    if favourite_fruit != fruits:
        fruits.append(favourite_fruit)
    else:
        print("The fruit exist already.")
