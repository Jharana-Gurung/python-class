# Create a function is_palindrome that takes a string and returns True if it is a palindrome (reads the same forwards and backwards), False otherwise. Ignore case and non-alphabetic characters.
# Example:

# Input: is_palindrome("A man a plan a canal Panama")
# Output: True
# Input: is_palindrome("hello")
# Output: False


def is_palindrome(text):

    cleaned_text = ''.join(char.lower()
    for char in text if char.isalpha())

    return cleaned_text == cleaned_text[::-1]


print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
