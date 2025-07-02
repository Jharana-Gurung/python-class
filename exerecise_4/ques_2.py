def unique_chars(text):
    unique_list = []
    for char in text:
        if char not in unique_list:
            unique_list.append(char)
    return len(unique_list)


print(unique_chars("hello"))
