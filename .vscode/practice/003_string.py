
#  Write a Python program to calculate the length of a string.
user_input = input("Type something: ")

string_length = len(user_input)

print("The length of what you typed is:", string_length)


# Write a Python function that takes a list of words and return the longest word and the 
# length of the longest one.
def find_longest_word(words):

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)


fruits = ["apple", "banana", "cherry", "watermelon"]
word, length = find_longest_word(fruits)

print("The longest word is:", word)
print("Length of the word is:", length)


# Write a Python program to remove characters that have odd index values in a given string
text = input("Enter text: ")
new_text = ""

for i in range(len(text)):
    if i % 2 == 0:
        new_text += text[i]

print("Result:", new_text)

