# Write a function reverse_string that takes a string as input and returns the string reversed.


def reverse_string(text):
    return text[::-1]


print(reverse_string("hello"))
print(reverse_string("Python"))

name = "swift"
# Approach 1
# reversed_name = name[::-1]

# Approach 2
characters = list(name)

ulto_characters = list(reversed(characters))

reversed_name = "".join(ulto_characters)

print(reversed_name)
