
# self vaneko paxi aayera banne object value rakhna
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("inside intro method.")
        print(self)


a = Animal("yoyo")
print("called outside the class.")
print(a)
a.intro()
