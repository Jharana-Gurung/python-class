# class Student:
#     college = "ICP"
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         return f"mero naam {self.name} ho and ma {self.college} ma padchu."

# student1 = Student("Ram")
# student2 = Student("Sita")

# print(student1.introduce())


# Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} bark: bho bho!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} myau garcha!"

# dog = Dog("Yoyo")
# cat = Cat("Princess")
# print(dog.speak())
# print(cat.speak())


# Class Methods and Variables

class Teacher:
    total_teachers = 0

    def __init__(self, name):
        self.name = name
        Teacher.total_teachers += 1

    @classmethod
    def get_total(cls):
        return f" all teachers: {cls.total_teachers}"


teacher1 = Teacher("Arjun")
teacher2 = Teacher("Prashant")
teacher3 = Teacher("Sanjog")
print(Teacher.get_total())


# Advanced Inheritance

# Using super() to extend parent functionality


class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} suru vayo."


class Car(Vehicle):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors

    def honk(self):
        return "pip pip !"


my_car = Car("Byd", 5)
print(my_car.start())
print(my_car.honk())
