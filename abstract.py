# python by default does not support abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("It is abstract class")

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("Start with kick")

class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("Self start")

class Car(Vehicle):
    def __init__(self,n, x):
        super().__init__(n)
        self.no_of_gears = 6
    def start(self):
        print("start with key")


bike = Bike(2, "black")
bike.start()

scooty = Scooty(3)
scooty.start()

Vehicle.display(2)