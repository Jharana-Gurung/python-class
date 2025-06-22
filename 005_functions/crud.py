# CRUD FUNCTION OF LIST

fruits = ["apple"]


def display_menu():
    print("""
_____________MENU_______________
1. Display fruits
2. Add fruits
3. Update fruits
4. Delete fruits
5. Existing Program
                """)


def add_fruits():
    count = int(input("Enter the number of fruits you want ro add:"))
    for i in range(1, count + 1):
        fruit_name = input("Enter the fruit name:")
        fruits.append(fruit_name)
    print("All the fruits are added sucessfully.")


def display_fruits():
    for fruit in fruits:
        print(fruit)


def update_fruits():
    display_fruits()
    update_index = int(input("Enter index to update: "))
    update_value = input("Enter the updated fruit name: ")
    fruits[update_index] = update_value
    print("Fruit updated successfully.")


def delete_fruits():
    display_fruits()
    deletion_index = int(input("Enter the index to delete: "))
    deleted_fruit = fruits.pop(deletion_index)
    print(f"The item '{deleted_fruit}' at index {deletion_index} is deleted.")


while True:
    display_menu()
    user_choice = input("Enter your choice:")
    if user_choice == "1":
        display_fruits()
    elif user_choice == "2":
        add_fruits()
    elif user_choice == "3":
        update_fruits()
    elif user_choice == "4":
        delete_fruits()
    elif user_choice == "5":
        print("Existing program.")
    else:
        print("invalid choice.")
