class Animal:
    def move(self):
        print("Animal is moving.")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Demo
def polymorphism_demo():
    movers = [Dog(), Fish(), Car(), Plane()]
    for mover in movers:
        mover.move()

polymorphism_demo()
