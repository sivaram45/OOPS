# Inheritance is a mechanism in which one class acquires the properties and methods of another class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!