class Vehicle:
    def move(self):
        print("Moving")

class Bike(Vehicle):
    pass

b = Bike()
b.move()
