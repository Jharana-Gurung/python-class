# Write a Python program to create a class and display the namespace of that class.
class MyClass:

    class_variable = 10

    def __init__(self, value):
        self.instance_variable = value

    def say_hello(self):
        print("Hello from MyClass!")


print(dir(MyClass))


# Define a Python function student(). Using function attributes display the names of all
# arguments.
def student(name, age, grade):
    pass


argument_names = student.__code__.co_varnames[: student.__code__.co_argcount]

print("Argument names:", argument_names)


# Write a Python class to reverse a string word by word.
class WordReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse_words(self):
        words = self.sentence.split()

        words.reverse()

        reversed_sentence = ' '.join(words)

        return reversed_sentence


my_sentence = "Hello how are you"
reverser = WordReverser(my_sentence)

print(reverser.reverse_words())
