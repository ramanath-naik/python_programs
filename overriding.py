#overriding is supported in python

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.sound())  # Output: Some sound
print(dog.sound())     # Output: Bark
print(cat.sound())     # Output: Meow
