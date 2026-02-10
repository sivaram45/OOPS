# Polymorphism is the ability of an object to take many forms. It allows objects of different types to be treated as instances of the same type through a common interface.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())   # Output: Woof! Meow!   
    