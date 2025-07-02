def greet(** kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]     # get garyo vane chai none aaucha key value error dinna

    print(f"My first name is {first_name}")
    print(f"My middle name is {middle_name}")
    print(f"My last name is {last_name}")


result = greet(
    first_name="Jharana",
    middle_name="Maya",
    last_name="Gurung"
    )
