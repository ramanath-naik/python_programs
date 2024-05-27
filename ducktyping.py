#Duck typing

class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swimming!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def swim(self):
        print("I'm swimming like a duck!")

def in_the_pond(duck):
    duck.quack()
    duck.swim()

# Both Duck and Person can be passed to in_the_pond function
duck = Duck()
person = Person()

in_the_pond(duck)  
in_the_pond(person)  
